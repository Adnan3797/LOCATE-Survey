This readme is about DOTA dataset.

## DOTA Dataset Visualization

Below is an example visualization of the DOTA dataset:

![DOTA Example Visualization](https://github.com/EngrKaleemUlah/LOCATE-Survey/blob/main/DOTA/Error%20Images/DOTAMissing1.png)

_Figure: Sample image from the DOTA dataset with annotated objects._


---

# 🧪 DOTA Dataset – Error Type Visual Examples

This document provides visual illustrations of common annotation errors identified in the DOTA dataset. These categories are based on our in-depth analysis and are meant to guide better understanding and diagnosis of dataset quality.

> 📂 Place your images in the `Error Images/` directory and update the file names as necessary.

---

## 🔴 1. Incorrect Labels

**Definition:** Objects are incorrectly labeled, resulting in false positives or class confusion.

| Image                                    | Caption                                                    |
| ---------------------------------------- | ---------------------------------------------------------- |
| ![](images/errors/incorrect_label_1.png) | ✖ Aircraft labeled as "helicopter" — incorrect class.      |
| ![](images/errors/incorrect_label_2.png) | ✖ Small car tagged as "truck", indicating label confusion. |

---

## 🟠 2. Localization Error

**Definition:** Bounding boxes are inaccurately placed, failing to tightly or correctly enclose the object.

| Image                                       | Caption                                                               |
| ------------------------------------------- | --------------------------------------------------------------------- |
| ![](images/errors/localization_error_1.png) | 📏 Bounding box misses part of the airplane wing — poor localization. |
| ![](images/errors/localization_error_2.png) | 📏 Box is too large and includes background — imprecise annotation.   |

---

## 🟡 3. Duplicates

**Definition:** Multiple overlapping bounding boxes are drawn around the same object.

| Image                              | Caption                                                   |
| ---------------------------------- | --------------------------------------------------------- |
| ![](images/errors/duplicate_1.png) | 🔁 Duplicate boxes drawn over the same building instance. |
| ![](images/errors/duplicate_2.png) | 🔁 Ship annotated twice, leading to redundant labels.     |

---

## 🔵 4. Inconsistent Annotations

**Definition:** Annotation practices vary across similar images or object types.

| Image                                 | Caption                                                       |
| ------------------------------------- | ------------------------------------------------------------- |
| ![](images/errors/inconsistent_1.png) | ⚠ Varying box sizes for similar objects across frames.        |
| ![](images/errors/inconsistent_2.png) | ⚠ Same object labeled inconsistently across different images. |

---

## ⚫ 5. Non-Existing Objects

**Definition:** Annotations are drawn around areas where no actual object is present.

| Image                                 | Caption                                                   |
| ------------------------------------- | --------------------------------------------------------- |
| ![](images/errors/non_existing_1.png) | ❌ Annotation present, but no object visible in this area. |
| ![](images/errors/non_existing_2.png) | ❌ False bounding box on background pixels.                |

---

## ⚪ 6. Challenging and Debatable

**Definition:** Objects are very hard to detect — even for human annotators.

| Image                                | Caption                                                       |
| ------------------------------------ | ------------------------------------------------------------- |
| ![](images/errors/challenging_1.png) | ❓ Object partially occluded, making annotation uncertain.     |
| ![](images/errors/challenging_2.png) | ❓ Low contrast or small size makes the object barely visible. |

---

## ✅ How to Use

* Replace the placeholder image paths (`images/errors/*.png`) with your actual error samples.
* Make sure your filenames match the patterns above or rename them accordingly.
* Use this as a quick reference to understand, debug, or audit the DOTA annotations.

---

Let me know if you’d like me to automatically generate this file from a list of image names or help create the folder structure for your dataset!
