PICTURES = visibility_visibility_100kev.png visibility_S00618.png profile_S00613.png

all: $(PICTURES)

visibility_visibility_100kev.png: visibility_100kev.hdf5 plot_visibility_pgf.py
	python plot_visibility_pgf.py --steps 25 --pixel 510 $<

visibility_S00618.png: S00618.hdf5 plot_visibility_pgf.py
	python plot_visibility_pgf.py --steps 25 --pixel 510 $<

profile_S00613.png: S00613.hdf5 plot_profile.py
	python plot_profile.py $<
