import SimpleITK as sitk
import numpy as np
import cv2
from scipy import ndimage
from skimage import morphology
import typing
from pathlib import Path
from pydicom import dcmread
from pydicom.dataset import FileDataset
from pydicom.dicomdir import DicomDir


class PreProcessor:
    """
    this class uses preprocessing methods on the dicom input. the preprocessing methods are:
    - removing most of the artifacts and all the neck images
    - centering the images

    HOW TO:
        path = dir/to/input_series
        preprocessor = PreProcessor()
        preprocessed_series, headers = preprocessor.preprocess(path)
    """

    @staticmethod
    def read_dcm(file_path: Path) -> typing.Tuple[np.ndarray, typing.Union[FileDataset, DicomDir]]:
        """
        this method makes the dicom images to numpy array and also it reads the header of the dicoms.
        Args:
            file_path(Path): the path to each dicom
        Returns:
             Tuple:
                - image(np.ndarray): dicom is read as numpy array
                - header(FileDataset): the header of the dicom.
        """
        header = dcmread(str(file_path), stop_before_pixels=True)
        image = sitk.ReadImage(str(file_path))
        image = sitk.GetArrayFromImage(image)[0]
        return image, header

    @staticmethod
    def create_mask(image: np.ndarray) -> typing.List[typing.Union[bool, np.ndarray]]:
        """
        this method creates a mask from the input image
        Args:
            image(np.ndarray): the numpy image from dicom file
        Returns:
            mask(np.ndarray): True False mask
        """
        brain_image = np.clip(image, 0, 80)
        segmentation = morphology.dilation(brain_image, np.ones((7, 7)))
        segmentation = ndimage.binary_fill_holes(segmentation)

        labels, label_nb = ndimage.label(segmentation)

        label_count = np.bincount(labels.ravel().astype(np.uint8))
        label_count[0] = 0

        mask = labels == label_count.argmax()
        mask = morphology.dilation(mask, np.ones((1, 1)))
        mask = ndimage.binary_fill_holes(mask)
        mask = morphology.dilation(mask, np.ones((3, 3)))
        mask = np.uint8(mask)
        return mask

    @staticmethod
    def detect_allblack_slices(mask):
        a = np.count_nonzero(mask)
        if a == (mask.shape[0] * mask.shape[1]) or a < 510:
            out = True
        else:
            out = False
        return out

    @staticmethod
    def remove_neck(mask: np.ndarray) -> typing.Tuple[int, int, int, int, float]:
        """
        this method removes the neck images from morphological operations and bounding box
        Args:
            mask(np.ndarray): True False mask from mask creator
        Returns:
            Tuple:
                - x(np.float64): the x coordinate of the bounding box
                - y(np.float64): the y coordinate of the bounding box
                - w(np.float64): the width of the bounding box
                - h(np.float64): the height coordinate of the bounding box
                - angle(np.float64): the output angle of fitellipse
        """
        contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key=cv2.contourArea)
        (a, b), (MA, ma), angle = cv2.fitEllipse(c)
        x, y, w, h = cv2.boundingRect(mask)
        return x, y, w, h, angle

    @staticmethod
    def center(image: np.ndarray, x: int, y: int, w: int, h: int) -> np.ndarray:
        """
        shifting the image to the center of a black background
        Args:
            - image(np.ndarray): the image from input dicom
            - x(np.float64): the x coordinate of the bounding box
            - y(np.float64): the y coordinate of the bounding box
            - w(np.float64): the width of the bounding box
            - h(np.float64): the height coordinate of the bounding box
        Returns:
            shifted(np.ndarray): the output image with the Hounsfield of input image
        """
        ROI = image[y:y + h, x:x + w]
        pic_back = ROI.min()
        shifted = np.ones(image.shape) * pic_back
        x = shifted.shape[1] // 2 - ROI.shape[1] // 2
        y = shifted.shape[0] // 2 - ROI.shape[0] // 2
        shifted[y:y + h, x:x + w] = ROI
        return shifted

    def preprocess(self, path: str) -> typing.Tuple[np.ndarray, typing.List[typing.Union[FileDataset, DicomDir]]]:
        """
        Args:
            path(Path): input path to the dicom series
        Returns:
            preprocessed_series(np.ndarray): preprocessed images
            headers(list[FileDataset]): list of headers of each preprocessed image
        """

        output = []
        headers = []
        dicoms = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(path)

        for file_ in dicoms:
            image, header = self.read_dcm(file_)
            out_mask = self.create_mask(image)
            is_all_black = self.detect_allblack_slices(out_mask)
            if is_all_black is False:
                x, y, w, h, angle = self.remove_neck(out_mask)
                shifted = self.center(image, x, y, w, h)
                headers.append(header)
                if ((40 < angle < 135) and (w > 1.4 * h)) or (h > 4 * w):
                    output.append([False, shifted])
                else:
                    output.append([True, shifted])
            else:
                output.append([False, out_mask])

        reversed_output = reversed(output)
        indexes = []
        for ind, out in enumerate(output):
            if out[0] is True:
                indexes.append(ind)
                break
        for ind, out in enumerate(reversed_output):
            if out[0] is True:
                ind = len(output) - ind
                indexes.append(ind)
                break

        output = output[indexes[0]:indexes[1]]
        final_output = []
        for out in output:
            final_output.append(out[1])
        preprocessed_series = np.array(final_output)
        return preprocessed_series, headers
