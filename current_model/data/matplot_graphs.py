import matplotlib.pyplot as plt

def plot_graph(data_1, data_2, integrator_1, integrator_2):
    
    try:
        plt.style.use(["science", "notebook", "grid"])
    except:
        plt.style.use("ggplot")

    groups = [
        (data_1, "group 0", integrator_1, "#FF0000"),
        (data_2, "group 1", integrator_2, "#0000FF"),
    ]
    figure, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    figure.suptitle("Energy Change over Time")

    for axis, method in zip(axes[:2], ("euler", "RK4")):
        matching_groups = [group for group in groups if group[2].casefold() == method.casefold()]
        for data, group_name, integrator, color in matching_groups:
            axis.plot(data.time, data.change, color=color, label=f"{group_name} ({integrator})")
        if matching_groups:
            axis.legend()
        else:
            axis.text(0.5, 0.5, f"No group is using {method}", ha="center", va="center", transform=axis.transAxes)
        axis.set_title(method)
        axis.set_ylabel("% Energy Change")

    combined_axis = axes[2]
    for data, group_name, integrator, color in groups:
        combined_axis.plot(data.time, data.change, color=color, label=f"{group_name} ({integrator})")
    combined_axis.set_title("Combined")
    combined_axis.set_xlabel("Time")
    combined_axis.set_ylabel("% Energy Change")
    combined_axis.legend()

    figure.tight_layout()
    plt.show()
