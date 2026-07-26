import torch
from torchvision import models
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# =========================================================
# 1. LOAD PRE-TRAINED RESNET50 MODEL
# =========================================================

print("Loading ResNet50 model...")

weights = models.ResNet50_Weights.DEFAULT
model = models.resnet50(weights=weights)
model.eval()

print("Model loaded successfully!")


# =========================================================
# 2. IMAGE PREPROCESSING
# =========================================================

preprocess = weights.transforms()


# =========================================================
# 3. LOAD IMAGE
# =========================================================

image_path = "image.jpg"

try:
    image = Image.open(image_path).convert("RGB")
except FileNotFoundError:
    print("\nERROR: image.jpg was not found!")
    print("Please put image.jpg in the same folder as project_4.py")
    exit()


# =========================================================
# 4. PREPARE IMAGE
# =========================================================

input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)


# =========================================================
# 5. IMAGE RECOGNITION
# =========================================================

print("\nAnalyzing image...")

with torch.no_grad():
    output = model(input_batch)


# =========================================================
# 6. CALCULATE PROBABILITIES
# =========================================================

probabilities = torch.nn.functional.softmax(output[0], dim=0)


# =========================================================
# 7. GET TOP 5 PREDICTIONS
# =========================================================

top5_probabilities, top5_indices = torch.topk(probabilities, 5)


# =========================================================
# 8. GET IMAGE CLASS NAMES
# =========================================================

categories = weights.meta["categories"]


# =========================================================
# 9. STORE RESULTS
# =========================================================

class_names = []
confidence_scores = []

for i in range(5):
    class_name = categories[top5_indices[i]]
    confidence = top5_probabilities[i].item() * 100
    class_names.append(class_name)
    confidence_scores.append(confidence)

best_prediction = class_names[0]
best_confidence = confidence_scores[0]


# =========================================================
# 10. PRINT RESULTS IN TERMINAL
# =========================================================

print("\n" + "=" * 65)
print("              AI IMAGE RECOGNITION SYSTEM")
print("=" * 65)

for i in range(5):
    print(f"{i + 1}. {class_names[i]} --> {confidence_scores[i]:.2f}%")

print("=" * 65)
print("\nFINAL PREDICTION")
print(f"Object     : {best_prediction}")
print(f"Confidence : {best_confidence:.2f}%")
print("=" * 65)


# =========================================================
# 11. COLORS
# =========================================================

background   = "#0B1020"
card_color   = "#151D32"
card_border  = "#263354"
purple       = "#8B5CF6"
cyan         = "#22D3EE"
white        = "#F8FAFC"
light_text   = "#CBD5E1"
green        = "#34D399"


# =========================================================
# 12. FIGURE + GRIDSPEC LAYOUT (no overlap, always proportional)
# =========================================================
# GridSpec automatically reserves fixed row/column space, so the
# image card and the predictions card can NEVER overlap, no matter
# how the window is resized.

fig = plt.figure(figsize=(16, 9), facecolor=background)

gs = GridSpec(
    nrows=2,
    ncols=2,
    figure=fig,
    width_ratios=[1, 1.6],     # right column wider for chart
    height_ratios=[1.3, 1],    # top row taller for image + chart
    left=0.05, right=0.97,
    top=0.78, bottom=0.14,     # more room left for header AND footer
    wspace=0.18, hspace=0.32
)

# Header (kept separate from GridSpec, above everything)
fig.text(0.5, 0.955, "AI IMAGE RECOGNITION", ha="center", va="center",
          fontsize=26, fontweight="bold", color=white)
fig.text(0.5, 0.905, "Deep Learning Vision System", ha="center", va="center",
          fontsize=12, color=cyan)

# Footer
fig.text(0.5, 0.05, "Powered by PyTorch  •  ResNet50  •  Deep Learning",
          ha="center", fontsize=10, color=light_text)


# =========================================================
# 13. IMAGE CARD (top-left)
# =========================================================

ax_image = fig.add_subplot(gs[0, 0], facecolor=card_color)
ax_image.imshow(image)
ax_image.axis("off")

for spine in ax_image.spines.values():
    spine.set_visible(True)
    spine.set_color(card_border)
    spine.set_linewidth(2)

ax_image.set_title("INPUT IMAGE", fontsize=16, fontweight="bold",
                    color=cyan, pad=10)


# =========================================================
# 14. TOP 5 PREDICTIONS CARD (top-right)
# =========================================================

ax_predictions = fig.add_subplot(gs[0, 1], facecolor=card_color)

display_names = class_names[::-1]
display_scores = confidence_scores[::-1]

bars = ax_predictions.barh(display_names, display_scores,
                            height=0.55, color=purple, alpha=0.9)

for bar, score in zip(bars, display_scores):
    ax_predictions.text(
        bar.get_width() + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{score:.2f}%",
        va="center", fontsize=11, fontweight="bold", color=white
    )

ax_predictions.set_title("TOP 5 PREDICTIONS", fontsize=16,
                          fontweight="bold", color=cyan, pad=10)
ax_predictions.set_xlabel("Confidence (%)", fontsize=11, color=light_text)
ax_predictions.tick_params(axis="x", colors=light_text)
ax_predictions.tick_params(axis="y", colors=white)
ax_predictions.grid(axis="x", linestyle="--", alpha=0.2)

ax_predictions.spines["top"].set_visible(False)
ax_predictions.spines["right"].set_visible(False)
ax_predictions.spines["left"].set_visible(False)
ax_predictions.spines["bottom"].set_color(card_border)

# extra headroom so % labels never get cut off
ax_predictions.set_xlim(0, max(100, max(display_scores) + 15))


# =========================================================
# 15. FINAL PREDICTION CARD (bottom-left)
# =========================================================

ax_final = fig.add_subplot(gs[1, 0], facecolor=card_color)
ax_final.axis("off")

for spine in ax_final.spines.values():
    spine.set_visible(True)
    spine.set_color(purple)
    spine.set_linewidth(2)

ax_final.text(0.5, 0.82, "FINAL PREDICTION", ha="center",
              fontsize=15, fontweight="bold", color=cyan)
ax_final.text(0.5, 0.50, best_prediction, ha="center", va="center",
              fontsize=20, fontweight="bold", color=white, wrap=True)
ax_final.text(0.5, 0.16, f"{best_confidence:.2f}% CONFIDENCE", ha="center",
              fontsize=14, fontweight="bold", color=green)


# =========================================================
# 16. MODEL INFORMATION CARD (bottom-right)
# =========================================================

ax_info = fig.add_subplot(gs[1, 1], facecolor=card_color)
ax_info.axis("off")

for spine in ax_info.spines.values():
    spine.set_visible(True)
    spine.set_color(card_border)
    spine.set_linewidth(2)

ax_info.text(0.5, 0.85, "MODEL INFORMATION", ha="center",
             fontsize=15, fontweight="bold", color=cyan)
ax_info.text(0.5, 0.63, "MODEL", ha="center", fontsize=10, color=light_text)
ax_info.text(0.5, 0.50, "ResNet50", ha="center", fontsize=14,
             fontweight="bold", color=white)
ax_info.text(0.5, 0.30, "DATASET: ImageNet", ha="center",
             fontsize=12, color=light_text)
ax_info.text(0.5, 0.12, "TOP 5 CLASSIFICATION", ha="center",
             fontsize=11, color=purple, fontweight="bold")


# =========================================================
# 17. SHOW DASHBOARD
# =========================================================

plt.show()