from setuptools import setup, find_packages

setup(
    name="torch_metrics-corrected",
    version="1.1.7",
    description="Metrics for model evaluation in pytorch",
    url="https://github.com/chinokenochkan/torch-metrics",
    author="Chi Nok Enoch Kan @chinokenochkan",
    author_email="kanxx030@gmail.com",
    packages=find_packages(include=["torch_metrics", "torch_metrics.*"]),
)
