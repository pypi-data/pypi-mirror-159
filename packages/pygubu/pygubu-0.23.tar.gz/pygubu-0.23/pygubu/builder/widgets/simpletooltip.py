from pygubu import BuilderObject, register_custom_property, register_widget
import pygubu.widgets.simpletooltip as tooltip


class SimpleTooltipBuilder(BuilderObject):
    allow_bindings = False
    layout_required = False

    def realize(self, parent):
        widget = parent.get_child_master()
        tooltip.create(widget, 'TOOLTIP AUTOTEXT')
        self.widget = widget
        return widget


_builder_id = 'pygubu.builder.widgets.simpletooltip'
register_widget(
    _builder_id, SimpleTooltipBuilder, 'SimpleTooltip', ('ttk', 'Pygubu Widgets')
)
