from django.forms import DateInput


class FengyuanChenDatePickerInput(DateInput):
    template_name = '../templates/teacher_access/widgets/fengyuanchen_datepicker.html'
