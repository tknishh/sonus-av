from setuptools import setup, find_packages

setup(
    name='sonus-av',
    version='0.1.0',
    author='Tanish Khandelwal',
    author_email='tanishqkhandelwaltqk011@gmail.com',
    description='A library to add voice and image input support to large language models (LLMs).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tknishh/sonus-av',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.0',
        'tensorflow-hub',
        'pytesseract',
        'Pillow',
        'openai',
        'speech_recognition',
        'deep_translator',
        'gtts',
        'playsound'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    keywords='llm, image processing, audio processing, large language models',
)