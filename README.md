# aeTools

**Production-oriented tools for Foundry Nuke, built to solve practical compositing problems.**

aeTools is a growing collection of custom gizmos and utilities developed by **Aitor Echeveste** for digital compositing, look development and VFX workflows.

The tools focus on recurring production problems such as cleanup, edge treatment, CG integration, relighting, motion, distortion, STMaps, UVs, refraction and volumetric lighting.

Most of them started as shot-specific solutions and evolved into reusable tools designed to remain lightweight, controllable and easy to integrate into existing Nuke scripts.

---

## Tool Collection

| Tool | Category | What it does |
| --- | --- | --- |
| [**aeVolumeRays**](./Aitor_Echeveste/aeVolumeRays) | Lighting | Physically inspired volumetric light rays directly inside Nuke |
| [**aeAutoMorph**](./Aitor_Echeveste/aeAutoMorph) | Motion / Morphing | Motion-aware morphing between two elements |
| [**aeShadows**](./Aitor_Echeveste/aeShadows) | Integration | Create, remove and adjust shadows in live-action plates |
| [**aeDirtCG**](./Aitor_Echeveste/aeDirtCG) | CG Integration | Procedural surface variation and dirt using position or Deep data |
| [**iSTMap**](./Aitor_Echeveste/iSTMap) | Distortion | Re-reference, invert and motion blur STMap transformations |
| [**aeRefracTHOR**](./Aitor_Echeveste/aeRefracTHOR) | Refraction | Generate geometry and camera-based refraction effects |
| [**aeRelight2D**](./Aitor_Echeveste/aeRelight2D) | Lighting | Create approximate relighting from 2D imagery |
| [**aeAnamorphic**](./Aitor_Echeveste/aeAnamorphic) | Lens | Add anamorphic distortion and focus breathing |
| [**aeFiller**](./Aitor_Echeveste/aeFiller) | Cleanup | Remove unwanted elements while preserving surface detail |
| [**aeBrokenEdges**](./Aitor_Echeveste/aeBrokenEdges) | Edges | Procedurally break matte edges using image information |
| [**aeBrokenShapes**](./Aitor_Echeveste/aeBrokenShapes) | Roto / Mattes | Add organic irregularity to shapes and masks |
| [**aePowerPin**](./Aitor_Echeveste/aePowerPin) | Tracking | Extended CornerPin workflow with offsets and guides |
| [**aeMotionBlur**](./Aitor_Echeveste/aeMotionBlur) | Motion | Generate or control motion blur from estimated or custom vectors |
| [**aeTransform**](./Aitor_Echeveste/aeTransform) | Transform | Lightweight transform workflow for everyday compositing |
| [**aePrefMaker**](./Aitor_Echeveste/aePrefMaker) | 3D Utility | Generate a Pref position pass directly inside Nuke |
| [**aeUVChart**](./Aitor_Echeveste/aeUVChart) | 3D Utility | Inspect, isolate and export UV layouts |

---

## Installation

### 1. Download the repository

Download the repository as a ZIP from GitHub, or clone it with Git:

```bash
git clone https://github.com/aitorecheveste/aeTools.git
```

### 2. Copy the tool folder

Copy the `Aitor_Echeveste` folder into your Nuke user directory.

**macOS / Linux**

```text
~/.nuke/Aitor_Echeveste
```

**Windows**

```text
%USERPROFILE%\.nuke\Aitor_Echeveste
```

Your setup should look roughly like this:

```text
.nuke/
├── init.py
└── Aitor_Echeveste/
    ├── init.py
    ├── menu.py
    ├── aeVolumeRays/
    ├── aeAutoMorph/
    ├── aeShadows/
    ├── aeDirtCG/
    └── ...
```

### 3. Add the package to Nuke

Open your main `.nuke/init.py` file and add:

```python
nuke.pluginAddPath("./Aitor_Echeveste")
```

If `init.py` does not exist yet, create it as a plain text file named `init.py`.

Restart Nuke after installation.

The package recursively adds its internal tool folders to Nuke's plugin path.

---

# Tools

## aeVolumeRays

**Volumetric lighting directly inside Nuke.**

aeVolumeRays generates cinematic volumetric light shafts using a physically inspired raymarching approach.

Instead of relying on a rendered volumetric pass, the effect can be created and art-directed directly during compositing.

### Key features

- Raymarched volumetric lighting
- GPU-accelerated processing
- Anisotropic light scattering
- Exponential light attenuation
- Shadow and occlusion control
- Atmospheric density control
- Procedural variation
- Interactive look development

### Useful for

Window light, god rays, headlights through atmosphere, spotlights, architectural lighting, forest shafts, fog, dust and other situations where visible light needs to interact with atmosphere.

---

## aeAutoMorph

**Motion-aware morphing between two images or elements.**

aeAutoMorph estimates motion between two inputs and uses the resulting vectors to progressively distort them towards each other.

Unlike a simple dissolve, the tool attempts to create spatial continuity between corresponding features before blending the images.

### Main controls

- **Morph** controls the geometric transition
- **Dissolve** controls the final image blend
- **Vector Detail** adjusts motion estimation
- **Blur Map** smooths the generated vector field
- Optional mask input
- GPU acceleration when available

### Useful for

Transitions, transformations, cleanup changes, temporal fixes and situations where a conventional dissolve reveals too much movement between two elements.

---

## aeShadows

**Create, remove or modify shadows while preserving plate detail.**

aeShadows is designed for situations where an existing shadow needs to be manipulated directly during compositing.

It separates shadow information from the underlying plate so its brightness and colour can be adjusted while retaining texture.

### Key features

- Add shadows
- Reduce or remove existing shadows
- Shadow brightness control
- Shadow colour adjustment
- Texture-preserving workflow
- Edge and softness refinement

### Useful for

Matching CG shadows to photography, reducing unwanted production shadows and introducing additional contact or environmental shadowing during integration.

---

## aeDirtCG

**Procedural surface complexity for CG integration.**

aeDirtCG generates procedural noise patterns that can be used to break up clean CG surfaces and introduce controlled colour and luminance variation.

The textures can remain spatially attached to the CG using position information rather than behaving like conventional screen-space noise.

### Key features

- Procedural noise generation
- Multiple independently adjustable noise patterns
- Colour and luminance variation
- Position-based workflow
- Deep workflow
- Motion blur support
- Noise preview outputs
- Dedicated precomp/output modes

### Useful for

Breaking perfectly clean renders, adding grime, subtle colour variation, weathering, surface complexity and other imperfections that help CG sit naturally beside photography.

---

## iSTMap

**More control over existing STMap transformations.**

iSTMap extends the standard STMap workflow so an existing transformation can be manipulated without rebuilding the original setup.

### Key features

- Change the transformation reference frame
- Invert the STMap transformation
- Apply vector-based motion blur

### Useful for

SmartVector workflows, cleanup, texture projection, tracked patches and any situation where an STMap transformation needs to be re-timed, reversed or blurred.

---

## aeFiller

**Cleanup while preserving the character of the original surface.**

aeFiller is a BlinkScript-powered cleanup tool designed to remove unwanted elements without producing an obviously softened or textureless patch.

It separates the larger-scale fill from the original surface information so texture and highlight detail can be restored afterwards.

### Key features

- Remove markers and unwanted plate elements
- Preserve high-frequency surface detail
- Recover highlights
- Offset or displace recovered detail
- BlinkScript processing

### Useful for

Tracking-marker removal, small object cleanup, skin or surface repairs and repetitive cleanup tasks where a conventional paint or blur-based fill destroys too much texture.

---

## aeRelight2D

**Approximate lighting changes without additional render passes.**

aeRelight2D derives surface variation from the image and uses it to produce a controllable directional lighting effect.

### Key features

- 2D relighting
- Adjustable light direction
- Emboss/depth approximation
- Surface smoothing controls
- No dedicated lighting render pass required

### Useful for

Smoke, atmosphere, clouds, textured surfaces and other elements where a subtle lighting change can help integration without requiring physically accurate 3D relighting.

---

## aeRefracTHOR

**Create controllable refraction effects from geometry and a camera.**

aeRefracTHOR provides a compositing-side approach to refraction using Nuke's 3D environment.

### Key features

- Geometry-driven refraction
- Camera-aware distortion
- Adjustable optical behaviour
- Art-directable glass-like effects

### Useful for

Glass, transparent objects, distorted surfaces and situations where additional refraction needs to be created or modified after rendering.

---

## aeAnamorphic

**Add controllable anamorphic lens behaviour to a composite.**

aeAnamorphic combines measured distortion characteristics with controls for simulating some of the optical behaviour associated with anamorphic lenses.

### Key features

- Anamorphic distortion
- Distortion based on real lens charts
- Automatic focus breathing
- Focus-driven controls

### Useful for

Matching CG or additional elements to anamorphic photography and introducing lens behaviour into otherwise overly clean imagery.

---

## aeBrokenEdges

**Introduce controlled irregularity into unnaturally perfect matte edges.**

aeBrokenEdges uses information from the underlying image together with procedural variation to create more natural edge breakup.

### Key features

- Lightweight edge processing
- Plate-aware breakup
- Procedural noise breakup
- Adjustable edge complexity

### Useful for

Rotoscoping, key refinement, CG integration and any matte whose mathematically perfect boundary makes the composite feel synthetic.

---

## aeBrokenShapes

**Break clean shapes into more organic silhouettes.**

aeBrokenShapes introduces procedural distortion into roto shapes and masks while providing controls over the amount and character of the breakup.

### Key features

- Procedural shape distortion
- Randomised variation
- Additional distortion controls
- Fast matte generation

### Useful for

Smoke mattes, grime, organic boundaries, damage, terrain, irregular masks and other cases where manually creating complex edges would be unnecessarily slow.

---

## aePowerPin

**An extended CornerPin workflow for production tracking tasks.**

aePowerPin adds controls that are frequently needed after generating a standard CornerPin.

### Key features

- Independent side offsets
- Perspective-aware adjustment
- Reference guides
- Designed around Nuke tracking workflows
- Compatible with CornerPin-style exports

### Useful for

Tracked patches, cleanup, screen inserts, projection preparation and situations where a technically correct CornerPin still requires additional art-directed adjustment.

---

## aeMotionBlur

**Generate additional motion blur from footage motion or custom direction.**

aeMotionBlur provides several approaches for creating and controlling motion blur when the existing image does not contain enough temporal information.

### Key features

- Motion estimation from footage
- Vector-based motion blur
- Custom directional motion
- Maskable blur

### Useful for

Fast-moving elements, transformed patches, cleanup, CG integration and elements that need to match the motion characteristics of the surrounding plate.

---

## aeTransform

**A lightweight transform tool for everyday compositing.**

aeTransform packages frequently used transform functionality into a compact setup intended to remain inexpensive inside larger scripts.

### Useful for

General compositing transformations where keeping the node graph lightweight and easy to manage is more important than building a larger custom setup.

---

## aePrefMaker

**Generate Pref data directly inside Nuke from geometry and a camera.**

aePrefMaker creates a reference position pass that can be used for position-based compositing workflows without requiring an additional render from 3D.

### Key features

- Geometry-based Pref generation
- Camera support
- UV handling
- Adjustable render quality

### Useful for

Procedural texture placement, position-driven effects, CG integration and preparing data for tools such as aeDirtCG.

---

## aeUVChart

**Inspect and export UV information directly inside Nuke.**

aeUVChart helps manage assets whose UVs are distributed across different coordinate regions.

### Key features

- Inspect UV regions
- Isolate specific UV areas
- Export UV templates

### Useful for

Texture work, projection preparation, paint workflows and debugging UV-dependent compositing setups.

---

# Updating aeTools

To update the package:

1. Download or pull the latest version of the repository.
2. Replace your existing `Aitor_Echeveste` folder.
3. Restart Nuke.

If you cloned the repository directly:

```bash
git pull
```

Individual tools are developed and updated independently, so the Git history is the best source for release activity.

---

# Reporting Issues

If you find a bug, please open a GitHub Issue.

Including the following information makes problems much easier to reproduce:

- Tool name and version
- Nuke version
- Operating system
- Description of the problem
- Steps to reproduce it
- Screenshot or error message when relevant
- Minimal example script when possible

Before reporting a problem, make sure you are using the latest version from this repository.

---

# About

These tools are developed by **Aitor Echeveste** for high-end compositing, technical workflows and visual development.

The collection is built around a simple principle:

**Solve recurring production problems with tools that remain fast, understandable and art-directable.**

More tools, breakdowns and technical content can be found at [aitorecheveste.com](https://aitorecheveste.com/).

---

## Feedback

If a tool improves your workflow, breaks on a newer Nuke version, or you find a better way to approach the problem, feedback is welcome.

Bug reports and technical discussion can be submitted through the repository's Issues section.
