from flask import render_template, flash, redirect, url_for, request
from app import app, db


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="Home")

@app.route('/computer-models/overview')
def modeloverview():
	return render_template('computer-models/overview.html', title="Computer Models")

@app.route('/computer-models/icesheet')
def icesheet_model():
	return render_template('computer-models/icesheet.html', title="Ice-Sheet Model")

@app.route('/computer-models/sealevel')
def sealevel_model():
	return render_template('computer-models/sealevel.html', title="Sea Level Model")



@app.route('/inputs/ice')
def ice():
	return render_template('inputs/ice.html', title="Ice Input")

@app.route('/inputs/geometry')
def geometry():
	return render_template('inputs/geometry.html', title="Geometry Input")

@app.route('/inputs/rheology')
def rheology():
	return render_template('inputs/rheology.html', title="Rheology Input")

@app.route('/inputs/icemargins')
def icemargins():
	return render_template('inputs/icemargins.html', title="Ice Margins Input")

@app.route('/inputs/topography')
def topography():
	return render_template('inputs/topography.html', title="Topography Input")

@app.route('/inputs/shearstress')
def shearstress():
	return render_template('inputs/shearstress.html', title="Shear Stress Input")