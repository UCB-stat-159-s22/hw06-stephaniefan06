#build environment and set kernel

.PHONY : env
env :
	conda env create -f environment.yml -p /srv/conda/envs/ligo
	bash -ic 'conda activate /srv/conda/envs/ligo;python -m ipykernel install --user --display-name "IPython -ligo"'


#create jupyter book
.PHONY : html
html:
	jupyter-book build .
    
.PHONY : html-hub
html-hub:
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo "Start the Python http server and visit:
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"

# clean the folders
.PHONY : clean
clean :
	rm -f audio/*
	rm -f figures/*
	rm -f _build