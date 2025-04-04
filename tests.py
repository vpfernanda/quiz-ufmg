from token import EQUAL

import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# 10 Novos testes
def test_create_invalid_points_range():
    with pytest.raises(Exception):
        Question("Valid title", points=0)
    with pytest.raises(Exception):
        Question("Valid title", points=500)

def test_remove_choice_by_id():
    q = Question("Example Question", 1)
    c1 = q.add_choice("A")
    c2 = q.add_choice("B")
    q.remove_choice_by_id(c1.id)
    assert len(q.choices) == 1
    assert q.choices[0].id == c2.id

def test_remove_all_choices():
    q = Question("Example Question", 15)
    q.add_choice("Choice1")
    q.add_choice("Choice2")
    q.remove_all_choices()
    assert q.choices == []

def test_set_correct_choices():
    q = Question("Question Example")
    c1 = q.add_choice("Wrong")
    c2 = q.add_choice("Right")
    q.set_correct_choices([c2.id])
    assert c1.is_correct is False
    assert c2.is_correct is True

def test_add_choice_with_invalid_text():
    q = Question("Pick one")
    with pytest.raises(Exception):
        q.add_choice("")
    with pytest.raises(Exception):
        q.add_choice("A" * 101)

def test_select_choices_with_correct_ids_only():
    q = Question("Example", 10, 3)
    c1 = q.add_choice("Right1")
    c2 = q.add_choice("Right2")
    c3 = q.add_choice("Wrong")
    c4 = q.add_choice("Right3")
    correct_ids = [c1.id, c2.id, c4.id]
    q.set_correct_choices(correct_ids)
    selected = q.select_choices(correct_ids)
    assert selected == correct_ids

def test_remove_choice_with_invalid_id_exception():
    q = Question("Example", 5)
    c1 = q.add_choice("Right1")
    wrong_id = c1.id + 100
    with pytest.raises(Exception):
        q.remove_choice_by_id(wrong_id)

def test_choices_id_generated_incrementally():
    q = Question("Example", 10, 3)
    c1 = q.add_choice("c1")
    c2 = q.add_choice("c2")
    c3 = q.add_choice("c3")
    assert c1.id == 1
    assert c2.id == c1.id + 1
    assert c3.id == c2.id + 1

def test_select_choices_exceeds_max_selection():
    q = Question("Example", 10, 1)
    c1 = q.add_choice("c1", True)
    c2 = q.add_choice("c2")
    selected_ids = [c1.id, c2.id]
    with pytest.raises(Exception):
        q.select_choices(selected_ids)

def test_set_correct_choices_with_invalid_id_exception():
    q = Question("Example", 1)
    c1 = q.add_choice("c1")
    wrong_id = [c1.id *3]
    with pytest.raises(Exception):
        q.set_correct_choices(wrong_id)






