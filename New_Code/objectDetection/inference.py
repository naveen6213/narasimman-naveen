from mmdet.apis import init_detector, inference_detector,show_result_pyplot
config_file = 'objectDetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

checkpoint_file = 'objectDetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
device = 'cpu'
# init a detector
model = init_detector(config_file, checkpoint_file, device=device)


def detect_object(image_path,output_path):
    result = inference_detector(model, image_path)
    model.show_result(image_path, result, out_file=output_path)
    return True