import argparse
import tensorflow as tf
from tensorflow.tools.graph_transforms import TransformGraph


def parse_options():
    parser = argparse.ArgumentParser(description='Convert pb')
    parser.add_argument('--input-path', type=str, help='path to the input pb file to transform', required=True)
    parser.add_argument('--output-path', type=str, help='path to the output pb file', required=True)

    return parser.parse_args()


def fixup(input_path, output_path):
    with tf.gfile.FastGFile(input_path, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        graph_def = TransformGraph(graph_def,
            ['image_tensor'],
            [
                'detection_boxes',
                'detection_classes',
                'detection_scores',
                'num_detections'
            ],
            [
                'sort_by_execution_order',
            ])
        with tf.gfile.FastGFile(output_path, 'wb') as f:
            f.write(graph_def.SerializeToString())


if __name__ == '__main__':
    args = parse_options()

    fixup(args.input_path, args.output_path)
