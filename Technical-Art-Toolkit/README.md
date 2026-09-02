# Technical Art Toolkit — Blender + Python

> A practical toolkit for improving and automating common 3D production workflows in Blender.

## 🎯 Goal

This project explores the **Technical Art** side of 3D production: using Python to reduce repetitive work, validate assets and scenes, generate controlled variations and create artist-facing utilities.

## Current Features

### Scene Validation

Checks the current Blender scene for common production issues:

- Inconsistent object names
- Empty mesh objects
- Meshes without assigned materials
- Objects with unapplied scale

The operator reports a compact summary in Blender and the console.

### Naming

Renames selected objects using a consistent prefix and numbered naming convention, useful for organizing batches of assets.

### Procedural Variations

Generates simple geometry variations using configurable parameters:

- Number of variations
- Seed
- Spacing
- Deterministic randomization

The same seed produces the same variation sequence, making procedural results reproducible.

## 🧠 Technical Concepts

- Blender Python API (`bpy`)
- Operators and panels
- Custom Scene properties
- Procedural generation
- Deterministic randomization
- Scene and asset validation
- Naming conventions
- Automation of repetitive production tasks
- Artist-facing tool design
- Modular Python package structure

## 📁 Structure

```text
Technical-Art-Toolkit/
├── README.md
├── blender_addon/
│   └── lvc4br_ta_toolkit/
│       ├── __init__.py
│       ├── operators.py
│       ├── procedural.py
│       ├── ui.py
│       └── examples/
│           └── README.md
└── examples/
```

## 🚀 Installation

1. Download or clone this repository.
2. In Blender, open **Edit > Preferences > Add-ons**.
3. Choose **Install...** and select the addon package/folder containing `lvc4br_ta_toolkit`.
4. Enable **Lvc4br Technical Art Toolkit**.
5. In the 3D Viewport, press `N` and open the **TA Toolkit** tab.

The project currently targets Blender 3.0+ and uses only Blender's built-in Python API.

## 🧪 Example Workflow

A typical test workflow is:

1. Create or import a few objects.
2. Run **Validate Scene** to identify common issues.
3. Use **Rename Selected** to standardize asset names.
4. Use **Procedural Tools** to generate controlled variations.
5. Repeat with different seeds to compare deterministic results.

See [`blender_addon/lvc4br_ta_toolkit/examples/README.md`](blender_addon/lvc4br_ta_toolkit/examples/README.md) for step-by-step examples.

## 🚧 Status

**v0.2 — Work in progress.**

The current version establishes the addon architecture and demonstrates three practical Technical Art concepts. Future modules can expand the toolkit into a broader production utility set.

## 🔭 Roadmap

- [x] Addon registration and UI
- [x] Scene validation foundation
- [x] Naming utility
- [x] Deterministic procedural generation
- [ ] Collection and scene organization tools
- [ ] Material utilities
- [ ] Export preparation helpers
- [ ] Automated validation report UI
- [ ] Example scenes and visual demonstrations
- [ ] Technical Art case study

## Direction

The project demonstrates the kind of work I want to pursue as a **Technical Artist**: connecting 3D production knowledge with programming to build reliable, reusable workflows for artists and production teams.

**Luca Toniolo — Lvc4br**