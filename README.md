# NAIRA_CLASSIFICATION

## Overview
In an era where automation is becoming increasingly prevalent, the need for accurate and efficient systems is in each and every sector is paramount. To contribute to this
technological advancement, I have developed a Naira classification model.This model aims to identify the denominations of Nigerian Naira banknotes, 
including 5, 10, 20, 50, 100, 200, 500, and 1000 Naira notes. Such a model can be seamlessly integrated into various automated systems, including cash deposit machines, 
currency sorting machines, and more.

## Dataset
The model was trained on a dataset consisting of the following number of images for each denomination:
- 137 images of 5 Naira notes
- 138 images of 10 Naira notes
- 236 images of 20 Naira notes
- 250 images of 50 Naira notes
- 278 images of 100 Naira notes
- 210 images of 200 Naira notes
- 277 images of 500 Naira notes
- 210 images of 1000 Naira notes

28 images were used for validation, except for 5 Naira notes, which had 20 validation images. Additionally, 8 images were reserved for testing each denomination.

## Model Architecture
The classification model employs transfer learning using MobileNet as the base architecture. With this approach, I achieved impressive results, with a training accuracy
of 90% and a validation accuracy of 87%.

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
