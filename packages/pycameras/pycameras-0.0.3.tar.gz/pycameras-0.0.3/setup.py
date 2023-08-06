from setuptools import setup, find_packages

VERSION = '0.0.3' 
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
        install_requires=['tensorflow >= 2.7.0', 'matplotlib>=3.5.1', 'numpy>=1.21.5', 'opencv-python>=4.5.5.62'], 
        keywords=['python', 'first package'],
        classifiers= [ ]
)