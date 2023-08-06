from setuptools import setup, find_packages

setup(
  name="Titter",
  version="1",
  author="Rosee-xx",
  author_email="Admin@draken.ltd",
  description="Twitter api",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/Rosee-xx/Malicious-pypip-package",
  project_urls={
    "GitHub": "https://github.com/Rosee-xx/Malicious-pypip-package",
    "Bug Tracker": "https://github.com/Rosee-xx/Malicious-pypip-package/issues",
  },
  license="MIT",
  keywords=["Twitter","Twitter-api", "twiter", "authentication"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  package_dir={"": "."},
  packages=find_packages(where="."),
  install_requires=['requests']
)
