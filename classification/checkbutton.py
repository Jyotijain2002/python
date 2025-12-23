from matplotlib.widgets import CheckButtons
import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax_check=fig.add_axes([0.05,.4,.2,.2])

check_box=CheckButtons(ax=ax_check,labels=['x','y'],actives=[True,True],label_props={'color': ['red', 'orange'],
                                      'fontsize': [16, 20]},
                         frame_props={'edgecolor': ['red', 'orange'],
                                      'facecolor': ['mistyrose', 'peachpuff']},
                         check_props={'color': ['darkred', 'darkorange']})
ax.set_visible(False)
plt.show()