import os		# interacting with OS 
import glob		# glob.glob(-) : return list 'file name', if satisfied condition.  
import argparse		# cmd interface	
import matplotlib	# draw chart and plot (Data Visualization package)

# Keras / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model				# trainning method(model)
from layers import BilinearUpSampling2D				# Upsampling for 2D input
from utils import predict, load_images, display_images
from matplotlib import pyplot as plt 				# import matplotlib, from matplotlib import pyploy as plt

# Argument Parser
parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='examples/*.png', type=str, help='Input filename or folder.')
args = parser.parse_args()

# Custom object needed for inference and training
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}

print('Loading model...')

# Load model into GPU / CPU
model = load_model(args.model, custom_objects=custom_objects, compile=False)

print('\nModel loaded ({0}).'.format(args.model))

# Input images
inputs = load_images( glob.glob(args.input) )
print('\nLoaded ({0}) images of size {1}.'.format(inputs.shape[0], inputs.shape[1:]))

# Compute results
outputs = predict(model, inputs)

#matplotlib problem on ubuntu terminal fix
#matplotlib.use('TkAgg')   

# Display results
# use matplotlib, pyplot
viz = display_images(outputs.copy(), inputs.copy())
plt.figure(figsize=(10,5))				# decide plot size
plt.imshow(viz)						# show image
plt.savefig('test.png')					# save 
plt.show() 						# show plow as process
