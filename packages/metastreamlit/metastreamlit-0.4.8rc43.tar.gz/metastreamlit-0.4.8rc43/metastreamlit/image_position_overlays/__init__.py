import os
import base64
from io import BytesIO
from pathlib import Path
import streamlit.components.v1 as components
from typing import Optional, Any, Dict, Sequence
from dataclasses import dataclass


from ..utils import image_to_url, declare_component


_component_func = declare_component(Path(__file__).absolute())

@dataclass
class OverlayPosition:
    """
    Position and dimensions of the overlay (in pixels)
    """
    x: int
    y: int
    width: int
    height: int

class ImagePositionOverlaysResult:
    def __init__(self, component_value: Dict[str, Any], origin: str) -> None:
        self._component_value = component_value
        self.origin = origin

    def __len__(self) -> int:
        return len(self._component_value['positions'])

    def __getitem__(self, idx: int) -> Optional[OverlayPosition]:
        if not isinstance(idx, int) or idx >= len(self) or idx < -len(self):
            raise KeyError(f"Invalid key: {idx}")
        pos_dict = self._component_value['positions'][idx]
        if pos_dict is None:
            return None
        return OverlayPosition(
            x=int(pos_dict['x']),
            y=int(pos_dict['y']),
            height=int(pos_dict['height']),
            width=int(pos_dict['width']),
        )


def image_position_overlays(background: Any, overlays: Sequence[Any], initialPositions: Optional[Sequence[Optional[Dict[str, Any]]]] = None, key=None, **kwargs: Any) -> ImagePositionOverlaysResult:
    """Create a new instance of "my_component".

    Parameters
    ----------
    background: str or PIL.Image
        The background image on which we want to position an overlay
    overlays: List[str or PIL.Image]
        Overlay images
    initialPositions:
        Initial positions for the overlays. Each position is a Dict with this format:
        {
            x: 25,
            y: 25,
            width: 50,
            height: 50
        }
    **kwargs: additional arguments are forwarded to the component.
        See https://github.com/DominicTobias/react-image-crop#props
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    ImagePositionOverlaysResult or None

    """

    assert len(overlays) > 0, "Must provide at least one overlay"
    if len(overlays) > 1:
        raise NotImplementedError("`image_position_overlays` only supports a single overlay at the moment")
    if initialPositions is not None:
        assert len(initialPositions) == len(overlays), f"Provided {len(overlays)} overlays, but {len(initialPositions)} initial positions"
    if initialPositions is None:
        initialPositions = [None] * len(overlays)

    component_value = _component_func(
        background=image_to_url(background),
        overlays=[image_to_url(overlay) for overlay in overlays],
        initialPositions=initialPositions,
        kwargs=kwargs,
        key=key,
        default=None
    )
    if component_value is None:
        return ImagePositionOverlaysResult({'positions': initialPositions}, origin="default")
    return ImagePositionOverlaysResult(component_value, origin="component")
