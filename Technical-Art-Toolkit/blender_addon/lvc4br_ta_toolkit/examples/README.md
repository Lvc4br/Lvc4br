# Technical Art Toolkit — Examples

These short examples demonstrate the three utilities included in the Blender add-on. Use a test scene and save a copy before renaming objects or generating variations.

## Validate a scene

1. Install and enable the add-on.
2. Open the 3D Viewport and press `N`.
3. Select **TA Toolkit** and click **Validate Scene**.
4. Review the report in Blender or its console.

The check looks for known issues such as inconsistent names, empty meshes, missing materials and unapplied scale. It does not certify a scene as production-ready.

## Generate procedural variations

1. Open **TA Toolkit → Procedural Tools**.
2. Set **Count**, **Seed** and **Spacing**.
3. Click **Generate Variations**.
4. Repeat with the same seed to check reproducibility, or change the seed to create a different sequence.

## Rename objects

1. Select only the objects to change.
2. Open **TA Toolkit → Naming**.
3. Click **Rename Selected** and enter a prefix in the operator panel.

## Scope

These examples describe manual workflows, not automated tests or finished portfolio scenes.