
# Linear Regression from Scratch

![Python](https://img.shields.io/badge/Python-181717?style=for-the-badge&logo=python)

## Overview

An implementation of simple linear regression using
gradient descent and pure Python, without external
machine learning libraries.

## Mathematical Foundation

$$
\hat{y} = wx + b
$$

- **w** — Weight
- **b** — Bias
- **x** — Input
- **ŷ** — Predicted output

### Loss Function

Mean Squared Error (MSE):

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

## Training Dataset

| Input (x) | Output (y) |
|-----------|------------|
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |
| 4 | 9 |
| 5 | 11 |

## Expected Results

| Parameter | Expected Value |
|-----------|----------------|
| Weight | ≈ 2.0 |
| Bias | ≈ 1.0 |
| Prediction (x = 6) | ≈ 13.0 |

## Implementation

- Object-oriented programming
- Gradient descent optimization
- Supervised learning
- No external dependencies

## How to Run

```bash
python3 model.py
```

## Requirements

Python 3

## Author

Andria Amiranashvili — AI Lab
