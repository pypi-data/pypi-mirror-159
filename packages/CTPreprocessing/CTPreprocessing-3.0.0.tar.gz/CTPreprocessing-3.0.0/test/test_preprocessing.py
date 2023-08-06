import pytest
from pathlib import Path
import numpy as np
import sys

sys.path.append('C:/Users/Azin/PycharmProjects/pre_project1')
from preprocessing.preprocess import PreProcessor
from pydicom.dataset import FileDataset


class TestPre:

    @pytest.fixture
    def input_directory(self):
        dir = r'C:\Users\Azin\Desktop\CQ500CT1 CQ500CT1\CT 2.55mm_1.2.276.0.7230010.3.1.3.296485376.1.1521714567.2079631'
        return dir

    @pytest.fixture
    def input_path(self):
        path = r'C:\Users\Azin\Desktop\CQ500CT1 CQ500CT1\CT 2.55mm_1.2.276.0.7230010.3.1.3.296485376.1.1521714567.2079631\1.2.276.0.7230010.3.1.4.296485376.1.1521714567.2079632.dcm'
        return path

    @pytest.fixture
    def pre(self):
        return PreProcessor()

    def test_read_dcm(self, pre, input_path):
        read_dcm_output = pre.read_dcm(input_path)
        assert len(read_dcm_output) == 2
        assert type(read_dcm_output[0]) == np.ndarray
        assert type(read_dcm_output[1]) == FileDataset

    def test_mask_creator(self, pre, input_path):
        image, header = pre.read_dcm(input_path)
        mask_creator_output = pre.create_mask(image)
        assert type(mask_creator_output) == np.ndarray

    def test_is_all_black(self, pre, input_path):
        image, header = pre.read_dcm(input_path)
        mask_creator_output = pre.create_mask(image)
        is_all = pre.detect_allblack_slices(mask_creator_output)
        assert type(is_all) == bool

    def test_neck_remover(self, pre, input_path):
        image, header = pre.read_dcm(input_path)
        mask = pre.create_mask(image)
        neck_remover_output = pre.remove_neck(mask)
        assert len(neck_remover_output) == 5
        for i in range(4):
            assert (type(neck_remover_output[i])) == int
        assert (type(neck_remover_output[4])) == float

    def test_centering(self, pre, input_path):
        image, header = pre.read_dcm(input_path)
        mask = pre.create_mask(image)
        neck_remover_output = pre.remove_neck(mask)
        centering_output = pre.center(image, neck_remover_output[0], neck_remover_output[1], neck_remover_output[2],
                                      neck_remover_output[3])
        assert type(centering_output) == np.ndarray

    def test_preprocess(self, pre, input_directory):
        preprocess_output = pre.preprocess(input_directory)
        assert len(preprocess_output) == 2
        assert type(preprocess_output[0]) == np.ndarray
        assert type(preprocess_output[1]) == list
