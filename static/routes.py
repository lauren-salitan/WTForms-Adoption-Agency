from flask import render_template, redirect, url_for, request
from . import app, db
from .models import Pet
from .forms import AddPetForm, EditPetForm

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data,
                      photo_url=form.photo_url.data, age=form.age.data,
                      notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_pet_form.html', form=form, pet=pet)
