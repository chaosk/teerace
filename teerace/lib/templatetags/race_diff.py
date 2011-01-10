from django import template
from race.models import Run
from annoying.functions import get_config

register = template.Library()

@register.simple_tag
def race_diff(run, compare_to=None, custom_green=None):
	if run == compare_to:
		# sneaky, we use it for race_diff(run, custom_green)
		compare_to = None
	if compare_to is None:
		user = run.user
		map_obj = run.map
		best_result = Run.objects.filter(map=map_obj, user=user).order_by('time')[0]
		diff = run.time - best_result.time
	else:
		diff = run.time - compare_to.time
	if diff > 0.0:
		style = 'red'
	else:
		style = 'green'
		if custom_green:
			return custom_green
	return '<span class="{0}">{1:+.{precision}f}</span>'.format(style, diff,
		precision=get_config('RESULT_PRECISION', 3))


@register.simple_tag
def diff_color(diff):
	if diff > 0.0:
		style = 'red'
	elif diff < 0.0:
		style = 'green'
	else:
		return '-'
	return '<span class="{0}">{1:+.{precision}f}</span>'.format(style, diff,
		precision=get_config('RESULT_PRECISION', 3))
	