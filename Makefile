#build environment and set kernel

.PHONY : env
env :
	conda env create -f environment.yml -p /srv/conda/envs/ligo
	bash -ic 'conda activate /srv/conda/envs/ligo;python -m ipykernel install --user --display-name "IPython -ligo"'


#build local jupyter book
.PHONY : html
html:
	jupyter-book build .

#create the jupyter book link
.PHONY : html-hub
html-hub:
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo Go to the _build/html folder and run "python -m http.server"
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"

# clean the folders
.PHONY : clean
clean :
	rm -f audio/*
	rm -f figures/*
	rm -f _build