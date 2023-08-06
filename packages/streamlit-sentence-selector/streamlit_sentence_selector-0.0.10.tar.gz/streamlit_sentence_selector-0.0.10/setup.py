import setuptools


try:
    import pypandoc
    long_description=pypandoc.convert("README.md",'rst')
except:
    long_description='A selector for a list of sentences or strings, and return a list of sentences or strings that you selected'

setuptools.setup(
    name="streamlit_sentence_selector",
    version="0.0.10",
    author="omnilab_xiaowu",
    author_email="1558359609@qq.com",
    description="A selector for a list of sentences or strings, and return a list of sentences or strings that you selected",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
