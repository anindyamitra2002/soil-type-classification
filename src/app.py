import gradio as gr
import numpy as np
import cv2
from model import classify_image

def main(img):
    img = cv2.resize(img, (224,224))
    img = img/255.0
    img = np.expand_dims(img, axis=0)
    label, accuracy = classify_image(img)
    print(label)
    out = {label: accuracy}
    return out

demo = gr.Interface(fn=main,
             inputs=gr.Image(),
             outputs=gr.Label(num_top_classes=1), allow_flagging='never')

if __name__ == "__main__":
    demo.launch(share=True)