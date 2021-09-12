lint:
 	# must be $$ because $ is make special character
	pycodestyle `find . | grep -v .venv | grep .py$$ | xargs`