# -*- coding: utf-8 -*-
# Copyright 2021 UuuNyaa <UuuNyaa@gmail.com>
# This file is part of MMD UuuNyaa Tools.

import bpy
from mmd_uuunyaa_tools.tuners import (lighting_tuners, material_adjusters,
                                      material_tuners)


class TuneLighting(bpy.types.Operator):
    bl_idname = 'mmd_uuunyaa_tools.tune_lighting'
    bl_label = 'Tune Lighting'
    bl_description = 'Tune selected lighting.'
    bl_options = {'REGISTER', 'UNDO'}

    lighting: bpy.props.EnumProperty(
        items=lighting_tuners.TUNERS.to_enum_property_items(),
    )

    @classmethod
    def poll(cls, _):
        return True

    def execute(self, context):
        lighting_tuners.TUNERS[self.lighting](context.collection).execute()
        return {'FINISHED'}


class FreezeLighting(bpy.types.Operator):
    bl_idname = 'mmd_uuunyaa_tools.freeze_lighting'
    bl_label = 'Freeze Lighting'
    bl_description = 'Freeze active lighting.'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return lighting_tuners.LightingUtilities(context.collection).find_active_lighting() is not None

    def execute(self, context):
        utilities = lighting_tuners.LightingUtilities(context.collection)
        lighting = utilities.find_active_lighting()
        utilities.object_marker.unmark(lighting, depth=1)
        context.collection.mmd_uuunyaa_tools_lighting.thumbnails = lighting_tuners.ResetLightingTuner.get_id()
        return {'FINISHED'}


class TuneMaterial(bpy.types.Operator):
    bl_idname = 'mmd_uuunyaa_tools.tune_material'
    bl_label = 'Tune Material'
    bl_description = 'Tune selected material.'
    bl_options = {'REGISTER', 'UNDO'}

    material: bpy.props.EnumProperty(
        items=material_tuners.TUNERS.to_enum_property_items(),
    )

    @classmethod
    def poll(cls, context):
        return context.object.active_material

    def execute(self, context):
        material_tuners.TUNERS[self.material](context.object.active_material).execute()
        return {'FINISHED'}


class AttachMaterialAdjuster(bpy.types.Operator):
    bl_idname = 'mmd_uuunyaa_tools.attach_material_adjuster'
    bl_label = 'Attach Material Adjuster'
    bl_description = 'Attach Adjuster to selected material.'
    bl_options = {'REGISTER', 'UNDO'}

    adjuster_name: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object.active_material

    def execute(self, context):
        material_adjusters.ADJUSTERS[self.adjuster_name](context.object.active_material).attach()
        return {'FINISHED'}


class DetachMaterialAdjuster(bpy.types.Operator):
    bl_idname = 'mmd_uuunyaa_tools.detach_material_adjuster'
    bl_label = 'Detach Material Adjuster'
    bl_description = 'Detach Adjuster from selected material.'
    bl_options = {'REGISTER', 'UNDO'}

    adjuster_name: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object.active_material

    def execute(self, context):
        material_adjusters.ADJUSTERS[self.adjuster_name](context.object.active_material).detach_and_clean()
        return {'FINISHED'}
