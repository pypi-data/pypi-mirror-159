# Autograde visualizer Streamlit component

## Development

```
cd autograde_visualizer/frontend
npm run start
```

```
streamlit run autograde_visualizer/__init__.py -- --local=...
```

## Publish

```
cd autograde_visualizer/frontend
npm run build
cd -
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
```