import matplotlib.pyplot as plt

def plot_graph(data_1, data_2, integrator_1, integrator_2):

    try:
        plt.style.use(["science", "notebook", "grid"])
    except Exception:
        plt.style.use("ggplot")

    groups = [
        (data_1, "group 0", integrator_1, "#FF0000"),
        (data_2, "group 1", integrator_2, "#0000FF"),
    ]

    figure, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    figure.suptitle("Energy Change over Time")

    # group 0 on top, group 1 in the middle
    for axis, (data, group_name, integrator, color) in zip(axes[:2], groups):
        axis.plot(data.time, data.change, color=color, label=f"{group_name} ({integrator})")
        axis.set_title(f"{group_name} - {integrator}")
        axis.set_ylabel("% Energy Change")
        axis.legend()

    # combined at the very bottom
    combined_axis = axes[2]
    for data, group_name, integrator, color in groups:
        combined_axis.plot(data.time, data.change, color=color, label=f"{group_name} ({integrator})")
    combined_axis.set_title("Combined")
    combined_axis.set_xlabel("Time")
    combined_axis.set_ylabel("% Energy Change")
    combined_axis.legend()

    figure.tight_layout()
    plt.show()
