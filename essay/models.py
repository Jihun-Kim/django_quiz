from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from quiz.models import Question
from django.db import models

@python_2_unicode_compatible
class Essay_Question(Question):

    correct = models.CharField(
        max_length=300, null=True, blank=True,
        help_text=_("correct "),
        verbose_name=_("correct"))

    def check_if_correct(self, guess):

        if self.correct == guess:
            return True
        else:
            return False

#    def check_if_correct(self, guess):
#        return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):

	if self.check_if_correct(guess):
            return guess
	else:
	    return guess + "   X"

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")

