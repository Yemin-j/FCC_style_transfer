# Standardized False Color Composite (SFCC) Generation for GEMS Wildfire Smoke Imagery  
### Using StyleID-based Deep Learning Style Transfer

This repository accompanies a research study that applies **StyleID** to  
**GEMS FCC (False Color Composite)** wildfire smoke imagery to improve  
visual consistency, tone stability, and smoke plume visibility across time-series satellite data.

The original StyleID code is available at:  
🔗 https://github.com/jiwoogit/StyleID  
(Please download `sd-v1-4.ckpt` from the original repository.)

---

## 📌 Research Motivation

Wildfire smoke is a major environmental hazard whose visual properties vary  
significantly depending on:

- Solar zenith angle (SZA)  
- Atmospheric scattering  
- Observation time  
- Aerosol concentration  
- Sensor noise  

As shown in the *FCC examples in the uploaded paper (page 8)*,  
the same wildfire event captured at different times of day  
shows **severe tone inconsistency**, causing:

- Difficulty in smoke boundary interpretation  
- Reduced reliability in visual monitoring  
- Poor generalization for deep learning–based smoke detection  
- Color variability that disrupts time-series analysis  

To address this, we introduce a **Standardized False Color Composite (SFCC)**  
using style transfer techniques optimized for scientific satellite imagery.

---

## 🎯 Research Objective

The goal of this repository is **not** to provide a general implementation of StyleID.  
Instead, this repository documents how StyleID was used in the following scientific task:

> **"Applying deep learning style transfer to standardize the color tone  
of GEMS wildfire smoke imagery while preserving structural content."**

Specifically, we evaluated whether StyleID can:

1. Reduce tone variability across multi-hour GEMS FCC data  
2. Preserve smoke plume shape, edge clarity, and fine aerosol structures  
3. Improve visual interpretability for wildfire monitoring  
4. Outperform traditional normalization or GAN-based style transfer models  

---

## 🛰️ Dataset: GEMS FCC Wildfire Imagery

As described in the paper (pp. 6–8) :contentReference[oaicite:0]{index=0}:

- Sensor: **GEMS (Geostationary Environment Monitoring Spectrometer)**  
- Bands used:
  - **Red:** 380 nm – 340 nm (ΔUV)
  - **Green:** 380 nm
  - **Blue:** 340 nm
- Region: Korean Peninsula  
- Case studies: Wildfire events from **2022, 2023, 2025**  
- Purpose: Visualizing UV-absorbing aerosols (smoke) using FCC  

Raw FCC images show strong temporal tone instability (Figure 3 in the paper).

---

## 🧠 Models Compared

This study compared **four tone-standardization methods**:

| Method | Type | Strengths | Weaknesses |
|--------|------|-----------|------------|
| **ECDF** | Statistical | Fast, stable | Fails to preserve smoke shape |
| **ReHistoGAN** | GAN-based | Good color harmonization | Texture breakup, blurred structure |
| **StyTR-2** | Transformer | Handles global tone | Patch discontinuity, unstable on satellite data |
| **SI-DM** | Diffusion | Best structure preservation, smooth tone | Slightly lower histogram matching in Red band |

> StyleID (StyTR-2) was included as one of the models tested.  
> The SI-DM model eventually performed best in satellite imagery context  
> but StyleID provided meaningful comparison for transformer-based style transfer.

---

## 🔬 Key Findings

### 1. **StyleID improves tone consistency across frames**
Based on multiple wildfire cases (Figure 7–9 in the paper), StyleID:

- Reduces abrupt color shifts  
- Harmonizes background tone  
- Generates smoother temporal transitions  

### 2. **Structural preservation is moderate**
As shown in close-up comparisons (Figure 5 and 6):

- Smoke boundaries are partially preserved  
- Some patch-level artifacts remain  
- Global tone application may override fine aerosol details  

### 3. **Quantitative metrics do not fully reflect visual quality**
From Table 3 in the paper:

- StyleID shows middle-range SSIM, LPIPS, FID  
- But satellite smoke structures require domain-specific qualitative evaluation  

### 4. **Overall role of StyleID**
StyleID served as a powerful baseline for transformer-based color style transfer but  
was not the best-performing model for smoke imagery (SI-DM ranked highest).  

However, StyleID still:

- Demonstrated strong tone harmonization  
- Provided stable style transfer without extreme distortions  
- Helped validate the viability of transformer-based SFCC generation  

---

## 📌 Research Conclusion (Summary)

According to the study conclusions (pp. 22–23) :contentReference[oaicite:1]{index=1}:

- Deep learning style transfer significantly enhances  
  **tone consistency and smoke visibility** in GEMS FCC imagery.  
- StyleID helped demonstrate the effectiveness of transformer-based  
  approaches in preserving global tonal patterns.  
- The best overall model was SI-DM,  
  but StyleID was essential in the comparative evaluation.  
- This work represents the **first systematic application of style transfer  
  to wildfire smoke visualization in geostationary satellite imagery**.  

---

## 🔗 Acknowledgements

This repository includes code from:

**StyleID: Learning Style Identity for Anime Character Generation**  
© Original authors — Licensed under **Apache License 2.0**  
https://github.com/jiwoogit/StyleID

The `sd-v1-4.ckpt` model **is not included**.  
Please download it from the original repository and place it under:

./models/ldm/stable-diffusion-v1/sd-v1-4.ckpt


---

## 📄 Citation

