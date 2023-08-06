# MetaAI Streamlit components

Install with `pip install metastreamlit`

## Components
### `template_component`

This is a basic components aimed at demonstrating how to create custom components in streamlit - taken from [streamlit's custom component template](https://github.com/streamlit/component-template).

```python
import streamlit as st
import metastreamlit as mst

num_clicks = mst.template_component("World", key=0)
st.markdown("You've clicked %s times!" % int(num_clicks))
```

### `audio_input`

Record some audio from the user

```python
import streamlit as st
import metastreamlit as mst

audio_data = mst.audio_input(key=0)
if audio_data is None:
    st.write("Please record something above")
else:
    st.write(f"This is what you recorded (len={len(audio_data.data)}) - type={audio_data.mime_type}")
    st.audio(audio_data.data)
```

### `image_input`

Get an image from the user (either uploaded or from a preset)

```python
import streamlit as st
import metastreamlit as mst

st.write("Select Image")
result = mst.image_input(
    initialDefaultPicture="https://source.unsplash.com/qDkso9nvCg0/600x799",
    presetImages=[
        "https://source.unsplash.com/2ShvY8Lf6l0/800x599",
        "https://source.unsplash.com/Dm-qxdynoEc/800x799",
        "https://source.unsplash.com/qDkso9nvCg0/600x799",
    ],
    key="123"
)
if result is None:
    st.write("No image selected")
else:
    st.write(f"Image source: {result.origin}, type = {result.mime_type}")
    st.image(result.get_pil_image())
```

### `image_crop`

Crop an image (either from a URL, or given a PIL.Image)

```python
import streamlit as st
import metastreamlit as mst
import PIL.Image
import numpy as np

st.header("With image=URL")
crop = mst.image_crop(image="https://source.unsplash.com/qDkso9nvCg0/600x799", key='url')
if crop is not None:
    st.write(f"Crop pos: ({crop.x}, {crop.y}) - width={crop.width}, height={crop.height}")

st.header("With image=PIL.Image")
np.random.seed(0)
random_array = np.random.randint(low=0, high=255, size=(250,250), dtype=np.uint8)
random_im = PIL.Image.fromarray(random_array)
crop = mst.image_crop(image=random_im, key='pil')
if crop is not None:
    st.write(f"Crop pos: ({crop.x}, {crop.y}) - width={crop.width}, height={crop.height}")
```

### `image_position_overlays`

Position an image A over a background image B, optionnaly allowing to resize image A as well.
Returns width, height and position of image A over image B - in pixels.

```python
import streamlit as st
import metastreamlit as mst
import PIL.Image
import numpy as np

result = mst.image_position_overlays(
    background="https://source.unsplash.com/qDkso9nvCg0/600x799",
    overlays=["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/449px-Cat_November_2010-1a.jpg"],
    initialPositions=[{
        'x': 25,
        'y': 25,
        'width': 128,
        'height': 256
    }],
    keepSelection=True, # Can't disable selection
    key='component')

st.write(f"Result from: {result.origin}")
pos0 = result[0]
if pos0 is not None:
    st.write(f"Result pos: ({pos0.x}, {pos0.y}) - width={pos0.width}, height={pos0.height}")

```

## Developing components

### Adding a new component

To create a new component `my_component`, follow these steps:
1. Copy `metastreamlit/template_component` to `metastreamlit/my_component`
2. Edit `metastreamlit/__init__.py` to add an import for your component, so users can call it from `metastreamlit.template_component` directly
2. Create an example file `examples/my_component.py` (that you can use for development as well!)

### Developing a component

To develop a component `my_component`, follow these steps:
1. Install metastreamlit in editable mode
```bash
pip install -e .
```
2. run npm:
```bash
cd metastreamlit/my_component
npm install
npm run start
```
3. Test it by running it within streamlit:
```bash
streamlit run examples/my_component.py
```
