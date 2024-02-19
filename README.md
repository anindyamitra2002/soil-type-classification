

# Soil Type Classification

## Overview
Soil type classification is pivotal for agricultural decision-making, guiding farmers in optimal crop selection and fertilizer application. Understanding soil characteristics ensures tailored agricultural practices, maximizing crop yield and minimizing environmental impact. Accurate classification enables precision farming, facilitating data-driven decisions for irrigation, nutrient management, and crop planning. This not only enhances agricultural productivity but also promotes sustainable practices, conserving resources and mitigating potential risks. In essence, soil type classification serves as a fundamental tool to empower farmers with actionable insights, fostering efficient and sustainable agriculture practices.

## Dataset Metadata

The dataset comprises a total of 2067 images, each belonging to one of the following 8 classes:

1. Chalky Soil
2. Mary Soil
3. Sand
4. Slit Soil
5. Alluvial Soil
6. Black Soil
7. Clay Soil
8. Red Soil

## Dataset Augmentation

The dataset augmentation process involved the following parameters:

- Rescale: 1./255
- Rotation Range: 20 degrees
- Width Shift Range: 0.2
- Height Shift Range: 0.2
- Zoom Range: 0.2
- Horizontal Flip: True
- Vertical Flip: True
- Fill Mode: Nearest

## Models

We have experimented with both Convolutional Neural Networks (CNNs) including custom architectures and pretrained models, as well as traditional machine-learning models.

## Performance Metrics

The models were evaluated using a test set of 418 images, and the performance metrics are recorded in the following table:

|     Model Name      |     Epochs    |     loss    |     Accuracy    |
|---------------------|---------------|-------------|-----------------|
|     VGG16           |     50        |     0.43    |     0.83        |
|     custom   CNN    |     10        |     0.70    |     0.76        |
|     DenseNet121     |     65        |     0.12    |     0.95        |
|     custom   CNN    |     20        |     0.21    |     0.81        |

## Getting Started

To reproduce the results or use the trained models, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/soil-type-classification.git
cd soil-type-classification
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
```bash
gradio src/app.py
```

3. Run the provided scripts or adapt them for your specific use case.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mention any credits, references, or sources of inspiration.

Feel free to explore, contribute, and adapt the code for your soil classification projects! If you have any questions or issues, please open an [issue](https://github.com/your-username/soil-type-classification/issues).

--- 

Customize the README file with your specific details, and make sure to include any additional information or sections relevant to your project.
