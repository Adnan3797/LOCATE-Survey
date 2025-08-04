## 📚 DOTA Dataset

The **DOTA (Dataset for Object Detection in Aerial Images)** dataset is widely used for object detection tasks in **remote sensing** imagery. While DOTA is a rich and comprehensive benchmark, like many large-scale datasets, it is not immune to annotation inconsistencies and labeling errors.

This **README** serves as a visual reference guide showcasing various types of common annotation errors found during an extensive analysis of the dataset. By understanding these issues, researchers and practitioners can:

Improve model robustness through targeted augmentation.

Identify sources of poor performance during training/evaluation.

Guide annotation correction or quality assurance workflows.

Below, each error category is defined and illustrated using real examples from the DOTA dataset.

## 🧾 DOTA Dataset Visualization

Below is an example visualization of the DOTA dataset:

![DOTA Example Visualization](https://github.com/EngrKaleemUlah/LOCATE-Survey/blob/main/DOTA/Error%20Images/DOTAMissing1.png)

_Figure: Sample image from the DOTA dataset with annotated objects._

---

# 🧪 DOTA Dataset – Error Type Visual Examples

This README provides visual illustrations of common annotation errors identified in the DOTA dataset. These categories are based on our in-depth analysis and are meant to guide better understanding and diagnosis of dataset quality.

---

## 🔴 1. Incorrect Labels

**Definition:** Objects are incorrectly labeled, resulting in false positives or class confusion.

![DOTA Incorrect Label Example](Error%20Images/IncorrectLabel1.png)
✖ "Bridge" is labeled as "Small Vehicle"
![DOTA Incorrect Label Example](Error%20Images/IncorrectLabel2.png)
✖ "Ship" tagged as "Small Vehicle", indicating label confusion.

---

## 🟠 2. Localization Error

**Definition:** Bounding boxes are inaccurately placed, failing to tightly or correctly enclose the object.

![DOTA Localization Error Example](Error%20Images/Localization1.png)
📏 Bounding box misses part of the airplane --> poor localization.
![DOTA Localization Error Example](Error%20Images/Localization2.png)
📏 Box is too short and ignores some part --> imprecise annotation.

---

## 🟡 3. Duplicates

**Definition:** Multiple overlapping bounding boxes are drawn around the same object.

| ![DOTA Duplicate Annotation Example](Error%20Images/Duplicate_1.png)  
🔁 Duplicate boxes drawn over the same ship instances.
| ![DOTA Duplicate Annotation Example](Error%20Images/Duplicate_2.png)
🔁 Soccer Ball annotated twice, leading to redundant labels.

---

## 🔵 4. Inconsistent Annotations

**Definition:** Annotation practices vary across similar images or object types.

| ![DOTA Inconsistent Annotation Examples](Error%20Images/InconsistentLocalization.png)
| ![DOTA Inconsistent Annotation Examples](Error%20Images/Localization2.png)
⚠ Same object labeled inconsistently across different images.
⚠ Varying box sizes for similar objects across images.

---

## ⚫ 5. Non-Existing Objects

**Definition:** Annotations are drawn around areas where no actual object is present.

| ![DOTA Non Exisiting DOTA Examples](Error%20Images/NonExisting1.png)
❌ Annotation present, but no object visible in this area.
| ![DOTA Non Exisiting DOTA Examples](Error%20Images/NonExisting2.png)
❌ False bounding box on background pixels.

---

## ⚪ 6. Challenging and Debatable

**Definition:** Objects are very hard to detect — even for human annotators.

| ![DOTA ChallengingAndDebatable Images](Error%20Images/ChallengingAndDebatable.png) |
❓ Object partially occluded, making annotation uncertain.  
❓ Low contrast or small size makes the object barely visible.

---
