# Face-Recognition-In-Video
A Face-Recognition-In-Video project that consist in applying face recognition inside video
to detect target faces.
	
	This project should be used as proposal for the capstone project of the Udacity's MLND.

	### Proposal ###
	(approx. 2-3 pages)
	
	
	*** Domain Background ***
	(approx. 1-2 paragraphs)

	In this section, provide brief details on the background information of the domain from which the project 
	is proposed. Historical information relevant to the project should be included. It should be clear how or 
	why a problem in the domain can or should be solved. Related academic research should be appropriately 
	cited in this section, including why that research is relevant. Additionally, a discussion of your personal 
	motivation for investigating a particular problem in the domain is encouraged but not required.
	
	
	*** Problem Statement ***
	(approx. 1 paragraph)

	In this section, clearly describe the problem that is to be solved. The problem described should be well 
	defined and should have at least one relevant potential solution. Additionally, describe the problem 
	thoroughly such that it is clear that the problem is quantifiable (the problem can be expressed in 
	mathematical or logical terms), measurable (the problem can be measured by some metric and clearly 
	observed), and replicable (the problem can be reproduced and occurs more than once).
	
	
	*** Datasets and Inputs *** 
	(approx. 2-3 paragraphs)

	In this section, the dataset(s) and/or input(s) being considered for the project should be thoroughly 
	described, such as how they relate to the problem and why they should be used. Information such as how 
	the dataset or input is (was) obtained, and the characteristics of the dataset or input, should be 
	included with relevant references and citations as necessary It should be clear how the dataset(s) or 
	input(s) will be used in the project and whether their use is appropriate given the context of the problem.
	
	
	*** Solution Statement *** 
	(approx. 1 paragraph)

	In this section, clearly describe a solution to the problem. The solution should be applicable to the 
	project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution 
	thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in 
	mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly 
	observed), and replicable (the solution can be reproduced and occurs more than once).
	
	
	*** Benchmark Model *** 
	(approximately 1-2 paragraphs)

	In this section, provide the details for a benchmark model or result that relates to the domain, problem
	statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods 
	or known information in the domain and problem given, which could then be objectively compared to the 
	solution. Describe how the benchmark model or result is measurable (can be measured by some metric and 
	clearly observed) with thorough detail.
	
	
	*** Evaluation Metrics *** 
	(approx. 1-2 paragraphs)

	In this section, propose at least one evaluation metric that can be used to quantify the performance of 
	both the benchmark model and the solution model. The evaluation metric(s) you propose should be 
	appropriate given the context of the data, the problem statement, and the intended solution. Describe 
	how the evaluation metric(s) are derived and provide an example of their mathematical representations 
	(if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed 
	in mathematical or logical terms).
	
	
	*** Project Design *** 
	(approx. 1 page)

	In this final section, summarize a theoretical workflow for approaching a solution given the problem. 
	Provide thorough discussion for what strategies you may consider employing, what analysis of the data 
	might be required before being used, or which algorithms will be considered for your implementation. 
	The workflow and discussion that you provide should align with the qualities of the previous sections. 
	Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in 
	describing the project design, but it is not required. The discussion should clearly outline your 
	intended workflow of the capstone project.

	https://github.com/udacity/machine-learning/blob/master/projects/capstone/capstone_proposal_template.md


## Applying the Udacity's proposal plan to this project
### I- Domain Background
________________________________________
Facilitate people identification had been a crucial challenge for a long time. From ID papers such as ID card to recent biometric methods, the techniques are still ongoing with improvement. 
With new technologies, we still need to introduce safe, easy and reliable methods for people identification. The goal is to match each face with the corresponding person.
We denote recent improvements in the field of computer science, specifically in the field of machine learning, deep learning and computer vision that we think they could allow a lot of enhancement for face recognition.
Some researches are still done on the subject. We could relate for example the recent research work of Brandon Amos, Bartosz Ludwiczuk and Mahadev Satyanarayanan from School of Computer Science of Carnegie Mellon University, in June 2016. They demonstrated how their open source face recognition library OpenFace open the possibilities for face recognition with mobile applications. Their process was built around the LFW (Labeled Faces in the Wild), a public dataset of more than 13000 Labeled Faces images from about 6000 people. 

My main goal with this project is to build a start to end application for face recognition in video using various technologies such as machine learning, deep learning, and mobile application building in python.
Generally, this requires to have the faces to recognize as input, but they may already be available in a given dataset (associated to a dataset like the LFW presented above) so that the application can compute necessary comparisons methods and give an efficient result. This project should also be applied to both live videos and recorded videos. 
At the end of the project, users should be able to install the application on their smartphone and recognize faces included in their local database using a live video capture with their smartphone or a recorded video. 


### II- Problem Statement
________________________________________
Nowadays several methods or technologies are used to perform face recognition. They are a part of the Identification and Authentication process for many infrastructure systems.
We have a need to secure our infrastructures so that only trusted persons could have access.
On the other hand, we also know that smartphones are expanded through the world. Everybody has a smartphone and a solution which includes it should be very practical in term of accessibility and easiness.  So why not use it for face recognition?
We think the combination of both, machine learning technologies for face recognition and smartphones should bring significant revolutions in the domain. For example using a simple smartphone we should know who can have access to a room or not. 
So, with this project I am going to create an app which can do face recognition using latest high-level computing technologies such as Convolutional Neural Networks and Support Vector Machine for classification.



### III- Datasets and Inputs
________________________________________
As for any machine learning problem, we need more data, relevant data to compute the face recognition process.
Indeed, from one hand we need a dataset of faces to recognize, and on the other hand we will need to detect and capture new faces (unseen faces) as the input of the machine learning process. Then in the process, the machine will use the captured face, compare it to the faces in the given dataset and provide a result of its comparison. In fact it will try to find the faces which match in the dataset.
So, the inputs for the whole process (unseen face images of the person to recognize) should be directly extracted from a live video or recorded video and passed through the process.
The dataset should be a set of target faces already available in a file (for example .jpg file), a directory (directory of image files), or a database (for example the LFW).
Each target person should already have at least 10 face images in its directory to improve the recognition process performance. But only one face must appear in each image. Then, these images will be joined to the LFW dataset mentioned above for a pre-processing where faces will be detected and aligned so that they could be filled into the Convolutional Neural Network input. 
Finally, the unseen face images will be applied to the Convolutional Neural Network output through the SVM algorithm and perform the recognition process.


### IV- Solution Statement
________________________________________
A solution to deploy face recognition using latest high-level computing technologies and smartphone application should be deep learning. 
Indeed, as explained in the previous section, face images should be transformed first through a pre-processing and given to the Convolutional Neural Network (CNN) as its input. Then the CNN will generate embeddings with them. Embeddings are a generic representation for anybody's face which reveals its unicity.
Finally, we could apply a supervised learning algorithm such as SVM to the embeddings to perform a test and determine if each target face image (unseen face image) matches with a name in the database. 
The SVM will give a score, the accuracy on the LFW dataset, which will represent in percentage how close the target face image is with a given face in the database (the closest face is returned). Let's note that it returns a score anyway as it chooses the closest face image in the database. So we have to consider low values as a mismatch. 
And once all is done we could build the mobile application using our deep learning implementation.


### V- Benchmark Model
________________________________________
To perform this task we could use OpenFace, a python free and open source face recognition library with deep neural networks which use pre-trained Convolutional Neural Network to facilitate the process. 
It allows creating a directory of face images for each person to recognize. At least 10 images per person produce good performance but we can use more. One important information here is that only one face must appear in each image. And there's no need to crop the image around the face, OpenFace will do that automatically. 
"So all we need to do ourselves is run our face images through their pre-trained network to get the 128 measurements for each face" and then recognize faces applying a new face image (unseen image) to the generated model classifier. 
Moreover, OpenFace is well adapted to face recognition with mobile applications. 
(See References 3)


### VI- Evaluation Metrics
________________________________________
The evaluation metric that can be used to quantify the performance of the deployed model is the Accuracy on the LFW (Labeled Faces in the Wild) Benchmark. 
The LFW is a public dataset of more than 13000 Labeled Faces images from about 6000 people. It is pre-trained by OpenFace to facilitate the recognition process and improve the convolutional neural network performance.
Indeed when we deploy the model, and pass a new picture with an unknown face to the classifier script, we get a prediction of the accuracy of the picture with the closest face in the database (which also include the new face images we have created). So, we must take this into account and consider faces with lowest scores as a mismatch. 



### VII- Project Design
________________________________________
The goal of this project is to build a face recognizer using OpenFace and then deploy final improved model into a mobile application to allow live face recognition such as the digit recognition of the Deep Learning project.

As you could see below the OpenFace is a Python and Torch implementation of face recognition with deep neural networks. Torch allows the network to be executed on a CPU or with CUDA.
![alt tag](https://github.com/Kjeanclaude/Face-Recognition-In-Video/blob/master/OpenFace%E2%80%99s%20project%20structure.png)

Figure 1: OpenFace’s project structure.

As shown in Figure 1, raw face images are prepared and trained with the dlib’s pre-trained detector. Then after some transformation (preprocessing, pose detection and alignment) these images are ready to pass through the network and be transformed into embeddings (Face representation).
The embedding is a generic representation for anybody's face. Unlike other face representations, this embedding has the nice property that a larger distance between two face embeddings means that the faces are likely not of the same person. This property makes clustering, similarity detection, and classification tasks easier than other face recognition techniques where the Euclidean distance between features is not meaningful.
Therefore, the SVM algorithm is applied to predict the accuracy of the recognition process.


#### 1- Contribution on the OpenFace library
==============================

We define below our contribution on the OpenFace library to adapt the face recognition to our need and build the intended application. 
Indeed, with this project we are going to try several improvements on the OpenFace project’s neural networks:
- using the "batch-represent.lua" file (***./batch-represent/batch-represent.lua***) which is the torch neural network file which generates the pre-trained LFW neural network. 
- also working on torch neural network in python files (***./openface/openface/torch_neural_net.lutorpy.py*** and ***./openface/openface/torch_neural_net.py***) which are used to generate embeddings. 
- trying to combine and test some tensorflow neural networks on the project.
- adapting the ***./demos/classifier.py*** python script to our project as using it we could test and tune several classifiers here including SVM with our own parameters’ value.
Finally we should choose the customized recognizer as the model to use.
The performance evaluation will be done on the same metric as previous (the Accuracy on the LFW) during the tests.

And then we will turn our face recognizer implementation in a multi-screen mobile application where we could: 
- create target faces' subfolders
- add target faces' images
- take live video of persons and recognize them
- select a recorded video of target persons and recognize target faces in
And this application should have multiple use case as we can imagine; identity control access to a meeting room, staff identification (for a big company of at least 1000 employees, we cannot know everyone), etc.

Another plus is the publishing of a detailed step by step guide of implementation of this kind of solution.



#### 2- Create a working face recognizer
==============================

Run the OpenFace scripts from inside the OpenFace root directory as below: 

##### 2.1- Pose detection and alignment (preprocessing) 

Here we should align the target person face images with the LFW dataset using dlib.

***./util/align-dlib.py ./training-images/ align outerEyesAndNose ./aligned-images/ --size 96***

This will create a new ***./aligned-images/*** subfolder with a cropped and aligned version of each of our test images.

##### 2.2- Generate the representations from the aligned images (neural network)

Here we should pass the aligned images to our customized network input. 

***./batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/***

This will create a new ***./generated-embeddings/*** sub-folder which will contain a CSV file with the embeddings for each face image. 

##### 2.3- Train the face detection model

Here we should apply to our customized classifier the embeddings.

***./demos/classifier.py train ./generated-embeddings/***

This will generate a new file called ***./generated-embeddings/classifier.pkl***. This file has the SVM model we'll use to recognize new faces.

At this point, we should have a working face recognizer.


#### 3- Recognize faces
==============================

This is the last step of our face recognition model building.
Now we have to get a new picture with an unknown face and pass it to the classifier script like this:

***./demos/classifier.py infer ./generated-embeddings/classifier.pkl your_test_image.jpg***

We should get a prediction that looks like this:

***=== /test-images/ jean-claude-01.jpg ===***

***Predict jean-claude with 0.73 confidence.***

In a video, each frame will be considered as an image and the recognition will be done with each new face or face position in the video.


#### 4- Build the mobile application
==============================

This is the final step of our face recognition application building.

Once we have created a face recognizer on our computer which works well, we must now convert it into a beautiful mobile application in python with graphic user interfaces.

These (Udacity’s) courses may help:

[Develop Your First Android Application in Python](https://hameedullah.com/develop-your-first-android-application-in-python.html)

[Python for Android Tutorial](http://blog.rhesoft.com/2014/07/17/python-for-android-tutorial-1-using-the-accelerometer/)

[TensorFlow Android Camera Demo](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android)

[Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036)

[Developing Scalable Apps in Python](https://classroom.udacity.com/courses/ud858)

[Android Development for Beginners](https://www.udacity.com/course/android-development-for-beginners--ud837)

[Android Basics: Multi-screen Apps](https://www.udacity.com/course/android-basics-multi-screen-apps--ud839)

[Android Basics: Data Storage](https://www.udacity.com/course/android-basics-data-storage--ud845)





### VIII- References
________________________________________

[OpenFace](https://cmusatyalab.github.io/openface/)

[Face recognition with deep neural networks](https://github.com/cmusatyalab/openface)

[Openface: A general-purpose face recognition library with mobile applications](http://hgpu.org/?p=16213)

[Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78#.w54pxa9mt)

[Tensorflow implementation of the FaceNet face recognizer](https://github.com/davidsandberg/facenet)

[Home surveillance system with facial recognition](https://github.com/pyannote/pyannote-video)

[Face detection, tracking and clustering in videos](https://github.com/BrandonJoffe/home_surveillance)

**Visualizing and Understanding Convolutional Networks** | Matthew D. Zeiler, Rob Fergus. | [Download here](https://arxiv.org/pdf/1311.290 1v3)

**Face Synthesis from Facial Identity Features** | Forrester Cole, David Belanger, Dilip Krishnan, Aaron Sarna, Inbar Mosseri, William T. Freeman. | [Download here](https://arxiv.org/pdf/1701.04851v1)

**Learning Detailed Face Reconstruction from a Single Image** | Elad Richardson, Matan Sela, Roy Or-El, Ron Kimmel. | Network model P.4 | [Download here](https://arxiv.org/pdf/1611.05053v1)

**Cost-Effective Active Learning for Deep Image Classification** | Keze Wang, Dongyu Zhang, Ya Li, Ruimao Zhang, Liang Lin. | Network Architecture P.5 | [Download here](https://arxiv.org/pdf/1701.03551v1)

**Deep Learning Features at Scale for Visual Place Recognition** | Zetao Chen, Adam Jacobson, Niko Sünderhauf, Ben Upcroft, Lingqiao Liu, Chunhua Shen, Ian Reid and Michael Milford
[Download here](https://arxiv.org/pdf/1701.05105)
