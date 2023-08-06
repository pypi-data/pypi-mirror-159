from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="interest_loan_0.1",
    version="1.0.0",
    description="A  Interest Calculator calculate loan interest rate etc.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Akshay311/InterestCalc",
    author="Akshay Thakare",
    author_email="thakarea686@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["package"],
    include_package_data=True,
)
