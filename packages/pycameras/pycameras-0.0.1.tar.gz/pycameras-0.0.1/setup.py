from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'CAMERAS Model Visulisation Technique'
LONG_DESCRIPTION = 'CAMERAS Model Visulisation Technique, simpler and more generalized keras implementaion of CAMERAS: Enhanced Resolution And Sanity preserving Class Activation Mapping for image Saliency. Jalwana, Akhtar, Mian, Bennamoun. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021. '

# Setting up
setup(
        name="pycameras", 
        version=VERSION,
        author="Subham Sahu",
        author_email="subhamsahu1120@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['tensorflow', 'matplotlib', 'numpy', 'cv2'], 
        keywords=['python', 'first package'],
        classifiers= [ ]
)