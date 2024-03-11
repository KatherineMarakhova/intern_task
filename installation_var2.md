# How to install Packages from a YAML File in Conda

1. Install Conda
2. Create a YAML File, for ex.:
```
name: myenv
channels:
  - defaults
dependencies:
  - numpy
  - pandas
  - scikit-learn
```
  
3. Use Conda to Create the Environment from the YAML File  
```conda env create -f environment.yaml```
4. Activate the Environment  
```conda activate myenv```
5. Verifying the Installation  
```conda list```

P.S. Также можно использовать pipdeptree



