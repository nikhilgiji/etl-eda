Giji, Nikhil Francis, 12303308  
Jose, Dona Maria, 12305194

1. Write down the value of your seed:  
   60

2. Write down the value of your number of epochs:    
25

3. What are the (voice) commands?  
'up' 'left' 'down' 'stop' 'no' 'right' 'yes' 'go 

4. What is the number of samples?  
8000 

5. What is the name of the first wav-file?  
The first command is "stop" , the name of the first file is 0b40aa8e_nohash_0.wav 

6. Split filenames into training, validation and test sets using a 80:10:10 ratio,
respectively. What is the number of training files?  
6400 

7. What is the sample rate for the WAV-file?  
16,000 Hz 

8. What is the test accuracy of your CNN?  
86.53 

9. Describe the classification process in your own words! What do you think are the
features used for classification?  
The speech recognition tutorial using tensorflow explains that the classification
process that involves training a deep neural network to accurately identify the 
type of sound based on its waveform representation. Initially, the sound's waveform
representation is transformed into a spectrogram with a Short-Time Fourier Transform. 
The CNN model is then fed with the spectrogram as input to classify the sound into 
one of several predefined categories.

      The CNN model consists of a few convolutional layers followed by max pooling layers, 
      a flatten layer, and some fully connected layers. The model's output layer uses a softmax 
      activation function to generate the predicted probabilities for each of the categories.

      The classification process utilizes features extracted from the audio waveform's 
      spectrogram representation to capture the sound's frequency and time-domain characteristics. 
      These features represent the distribution of energy across different frequencies and time 
      intervals. By learning the patterns and relationships between these features and their 
      corresponding labels in the training data, the CNN model is trained to make accurate predictions.

      Overall, the classification process involves extracting relevant features from the 
      audio data and training a model to identify the type of sound using these features. 
