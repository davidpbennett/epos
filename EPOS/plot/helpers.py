''' helpers '''
import os

def set_axes(ax, epos, Trim=False, Eff=False):
	ax.set_xlabel('Orbital Period [days]')
	if epos.RV:	ax.set_ylabel(r'Planet M sin i [M$_\bigoplus$]')
	else:		ax.set_ylabel(r'Planet Radius [R$_\bigoplus$]')

	if Trim:
		ax.set_xlim(epos.xtrim)
		ax.set_ylim(epos.ytrim)
	elif Eff:
		ax.set_xlim(epos.eff_xlim)
		ax.set_ylim(epos.eff_ylim)
	else:
		ax.set_xlim(epos.obs_xlim)
		ax.set_ylim(epos.obs_ylim)

	ax.set_xscale('log')
	ax.set_yscale('log')

	#xticks=[3, 10, 30, 100, 300]
	#ax.set_xticks(xticks)
	#ax.set_xticklabels(xticks)

	#yticks=[0.5, 1, 2, 4]
	#ax.set_yticks(yticks)
	#ax.set_yticklabels(yticks)
	
	pass

def set_pyplot_defaults():
	from matplotlib import rcParams
	#print rcParams
	rcParams.update({'font.size': 16})
	rcParams.update({'legend.fontsize': 'medium'})
	rcParams.update({'axes.linewidth': 2.0})
	rcParams.update({'lines.linewidth': 2.0})
	rcParams.update({'patch.linewidth': 2.0})
	rcParams.update({'xtick.major.size': 8.0})
	rcParams.update({'xtick.minor.size': 4.0})
	rcParams.update({'ytick.major.size': 8.0})
	rcParams.update({'ytick.minor.size': 4.0})
	rcParams.update({'xtick.major.width': 1.0})
	rcParams.update({'xtick.minor.width': 1.0})
	rcParams.update({'ytick.major.width': 1.0})
	rcParams.update({'ytick.minor.width': 1.0})
	rcParams.update({'lines.markeredgewidth': 2.0})

def save(plt, name, dpi=150):

	# make sure path exists
	ipath= name.rfind('/')
	if ipath!= -1:
		#print name[:ipath]
		if not os.path.isdir(name[:ipath]): os.makedirs(name[:ipath])
	
	plt.savefig(name+'.png',bbox_inches='tight', dpi=dpi)
	plt.close()