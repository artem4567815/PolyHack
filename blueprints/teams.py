from re import match
from flask import Blueprint
from flask import render_template, redirect, request
from helpers import requires_auth
from methods import get_teams_by_owner, get_team_by_id, get_games, get_game_by_id, create_team, is_owner, delete_player

teams_blueprint = Blueprint('teams', __name__)


@teams_blueprint.route('/')
@requires_auth
def my(user):
    return render_template('teams/index.html', teams=get_teams_by_owner(user.id))


@teams_blueprint.route('/<int:team_id>')
@requires_auth
def team(user, team_id):
    try:
        team = get_team_by_id(team_id)
    except:
        return redirect('/teams')

    if user.id != team.user_id:
        return redirect('/teams')

    return render_template('teams/team.html', team=team)


@teams_blueprint.route('/<int:team_id>/delete/<int:player_id>')
@requires_auth
def del_player(user, team_id, player_id):
    if not is_owner(team_id, user.id):
        return redirect('/teams')

    try:
        delete_player(team_id, player_id)
    except Exception:
        pass
    
    return redirect('/teams')


@teams_blueprint.route('/create', methods=['get'])
@requires_auth
def create_page(user):
    return render_template('teams/create.html', games=get_games())


@teams_blueprint.route('/create', methods=['post'])
@requires_auth
def create(user):
    team_name = request.form.get('team_name')
    game_id = request.form.get('game_id')

    if not team_name:
        return render_template('teams/create.html', games=get_games(), error="Введите имя команды")

    if not match('^(?!\s*$).+', team_name):
        return render_template('teams/create.html', games=get_games(), error="Имя не должно быть пустым")

    try:
        selected_game = get_game_by_id(game_id)
    except:
        return render_template('teams/create.html', games=get_games(), error="Выберите игру")

    create_team(team_name, user.id, selected_game.id)

    return redirect('/teams')