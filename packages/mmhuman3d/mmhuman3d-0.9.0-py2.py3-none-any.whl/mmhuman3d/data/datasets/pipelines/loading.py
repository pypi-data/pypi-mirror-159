import os.path as osp

import cv2
import mmcv
import numpy as np

from mmhuman3d.data.data_structures.smc_reader import SMCReader
from ..builder import PIPELINES


@PIPELINES.register_module()
class LoadImageFromFile(object):
    """Load an image from file.

    Required keys are "img_prefix" and "img_info" (a dict that must contain the
    key "filename"). Added or updated keys are "filename", "img", "img_shape",
    "ori_shape" (same as `img_shape`) and "img_norm_cfg" (means=0 and stds=1).
    Both "img_shape" and "ori_shape" use (height, width) convention.

    Args:
        to_float32 (bool): Whether to convert the loaded image to a float32
            numpy array. If set to False, the loaded image is an uint8 array.
            Defaults to False.
        color_type (str): The flag argument for :func:`mmcv.imfrombytes()`.
            Defaults to 'color'.
        file_client_args (dict): Arguments to instantiate a FileClient.
            See :class:`mmcv.fileio.FileClient` for details.
            Defaults to ``dict(backend='disk')``.
    """

    def __init__(self,
                 to_float32=False,
                 color_type='color',
                 file_client_args=dict(backend='disk')):
        self.to_float32 = to_float32
        self.color_type = color_type
        self.file_client_args = file_client_args.copy()
        self.file_client = None

    def __call__(self, results):
        if self.file_client is None:
            self.file_client = mmcv.FileClient(**self.file_client_args)

        if results['img_prefix'] is not None:
            filename = osp.join(results['img_prefix'], results['image_path'])
        else:
            filename = results['image_path']

        if filename.endswith('smc'):
            assert 'image_id' in results, 'Load image from .smc, ' \
                                          'but image_id is not provided.'
            device, device_id, frame_id = results['image_id']
            smc_reader = SMCReader(filename)
            img = smc_reader.get_color(
                device, device_id, frame_id, disable_tqdm=True)
            img = img.squeeze()  # (1, H, W, 3) -> (H, W, 3)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # BGR is used
            del smc_reader
        else:
            img_bytes = self.file_client.get(filename)
            img = mmcv.imfrombytes(img_bytes, flag=self.color_type)

        if self.to_float32:
            img = img.astype(np.float32)

        results['filename'] = filename
        results['ori_filename'] = results['image_path']
        results['img'] = img
        results['img_shape'] = img.shape[:2]
        results['ori_shape'] = img.shape[:2]
        num_channels = 1 if len(img.shape) < 3 else img.shape[2]
        results['img_norm_cfg'] = dict(
            mean=np.zeros(num_channels, dtype=np.float32),
            std=np.ones(num_channels, dtype=np.float32),
            to_rgb=False)
        return results

    def __repr__(self):
        repr_str = (f'{self.__class__.__name__}('
                    f'to_float32={self.to_float32}, '
                    f"color_type='{self.color_type}', "
                    f'file_client_args={self.file_client_args})')
        return repr_str
