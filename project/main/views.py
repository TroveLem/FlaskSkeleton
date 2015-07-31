from flask import Blueprint


####                ####
####    config      ####
####	            ####

#change the 'main' to more accurate name
main_blueprint = Blueprint(
	'main',__name__,
	template_folder ='templates'
)

####                ####
####    Routes      ####
####	            ####

@main_blueprint.route('/')
def home():
	#return
	pass