# NAIRA_CLASSIFICATION

## Overview
In an era where automation is becoming increasingly prevalent, the need for accurate and efficient systems in every sector is paramount. To contribute to this technological advancement, I have developed a **Naira Classification Model**.  

This model identifies the denominations of Nigerian Naira banknotes, including **₦5, ₦10, ₦20, ₦50, ₦100, ₦200, ₦500, and ₦1000**. The model can be integrated into various automated systems such as **cash deposit machines, currency sorting machines, and retail checkout systems**.

## Dataset
The model was trained on a dataset consisting of the following number of images for each denomination:

| Denomination | Training Images | Validation Images | Test Images |
|-------------|----------------|-------------------|-------------|
| ₦5          | 137            | 20               | 8           |
| ₦10         | 138            | 28               | 8           |
| ₦20         | 236            | 28               | 8           |
| ₦50         | 250            | 28               | 8           |
| ₦100        | 278            | 28               | 8           |
| ₦200        | 210            | 28               | 8           |
| ₦500        | 277            | 28               | 8           |
| ₦1000       | 210            | 28               | 8           |

You can access the dataset on Kaggle:  
[📂 Naira Nigerian Currency Dataset](https://www.kaggle.com/datasets/ismailismailtijjani/naira-nigerian-currency-dataset)

## Model Architecture
The model utilizes **transfer learning with MobileNet** as the base architecture. The training results are:

- **Training Accuracy:** 90%
- **Validation Accuracy:** 87%

Despite these results, some mismatch conflicts were observed, particularly between **₦20 and ₦50 notes**.

## Performance
It's noteworthy that human-level performance in Naira classification is nearly perfect, approaching 100%. Consequently, the model is expected to near human performance,
highlighting the importance of continuous improvement and refinement.
While the model achieved impressive results during testing, there were instances of mismatch conflict between denominations, particularly between
50 and 20 Naira notes, along with other minor issues. 

## Challenges
The primary challenge encountered in developing this model comes from the scarcity of a diverse and comprehensive dataset. The limited availability of varied images
representing different Naira denominations poses a significant obstacle to achieving optimal performance. The mismatch conflicts observed during testing, particularly 
between 50 and 20 Naira notes, along with other minor issues, can be directly attributed to this dataset deficiency. Addressing this challenge by acquiring a more extensive 
and diverse dataset will be paramount in improving the model's accuracy and generalizability.

---

## Installation & Usage

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-username/naira-classification.git
cd naira-classification
```

## Step 2: Install Dependencies

Ensure you have **Python 3.8+** installed, then run:


```sh
pip install -r requirements.
```

## Step 3: Download the Dataset
Download the dataset from **[Kaggle](https://www.kaggle.com/datasets/ismailismailtijjani/naira-nigerian-currency-dataset)** and extract it into the project directory.

## Step 4: Run the Application
Start the **Gradio** interface:

``` sh
python app.py
```
The application will launch a web interface where you can **upload and classify Naira notes**.

## Step 5: Test with the Dataset
To test the model:

1. **Open the Gradio UI.**  
2. **Upload an image** of a Naira note.  
3. Click **"Predict"** to see the classification result.  


## Future Improvements
- Expansion of the dataset: Acquiring a more extensive collection of Naira images to improve the model's performance.
- Fine-tuning and optimization: Continuously refining the model's architecture and training parameters to achieve even higher accuracy and efficiency.
- Deployment and integration: Integrating the model into real-world applications such as automated teller machines (ATMs), currency sorting systems, and retail checkout
  processes to streamline operations and enhance user experience.

## Collaboration
As a computer vision model developer, I acknowledge my limitations and recognize the importance of collaboration in making projects a reality. While I bring expertise 
in developing models and algorithms, I understand that collaborative efforts can enhance the scope and impact of projects.

I am open to collaboration on this project and others, leveraging the collective expertise of diverse individuals to overcome challenges and achieve shared goals. 
Whether you're a fellow developer, data scientist, software developer, domain expert, or enthusiast, I welcome collaboration opportunities to push the boundaries of
AI applications.

If you're interested in collaborating or have ideas for potential projects, feel free to reach out.

## Citation
The dataset utilized in this project was provided by EJAZTECH.AI, a company dedicated to gathering local datasets for AI applications, founded by me.
We acknowledge their invaluable contribution to the development of this model and other models by providing access to diverse and localized data, which played a 
crucial role in training and validating the NAIRA_CLASSIFICATION model. We express our gratitude to EJAZTECH.AI for their commitment to advancing AI research and
applications in Nigeria and beyond.

For further inquiries or collaboration opportunities, you can contact the company via their email address:
- Email: [ejaztech.ai@gmail.com]



