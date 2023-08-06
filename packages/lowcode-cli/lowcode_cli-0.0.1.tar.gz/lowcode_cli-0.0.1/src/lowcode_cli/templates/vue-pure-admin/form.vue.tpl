{% set fields = schema.properties.fields.properties %}
{% set field_names = get_field_names(schema) %}
{% set search_form_data = get_field_default_value(schema) %}
{% set default_value = get_field_default_value(schema) %}
{% set app_name = schema.properties.app.app_name or '' %}
{% set model_name = schema.properties.model.name or '' %}
{% set searchable_fields = get_searchable_fields(schema) %}
{% set filterable_fields = get_filterable_fields(schema) %}
{% set image_field_exists = image_field_exists(schema) %}
<template>
  <div>
    <el-card class="form-card">
      <el-form :model="formData" label-width="120px">
        {% for name, field in fields.items() %}
          {% if field.creatable == False %}
          {% continue %}
          {% endif %}
          <el-form-item label="{[ field.label or field.name ]}">
          {% if field.component %}
            {#            指定组件#}
            <component :is="component"/>
          {% else %}
            {#            根据数据类型推断组件#}
            {% if field.type == "string" %}
            <el-input
                {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
                v-model="formData.{[ name ]}" />
            {% elif field.type == "number" %}
            <el-input-number
                {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
                v-model="formData.{[ name ]}" />
            {% elif field.type == "date" %}
            <el-date-picker
                {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
                v-model="formData.{[ name ]}"
                type="date"
              />
            {% elif field.type == "datetime" %}
              <el-date-picker
                {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
                v-model="formData.{[ name ]}"
                type="datetime"
              />
            {% elif field.type == "single-select" %}
            {% elif field.type == "multi-select" %}
            <el-checkbox-group
                {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
                v-model="formData.{[ name ]}">
                {% for option in field.options or [] %}
                  <el-checkbox model-value="{[ option.value ]}" label="{[ option.label ]}">{[ option.label ]}</el-checkbox>
                {% endfor %}
            </el-checkbox-group>
            {% elif field.type == "image" %}
              <el-upload
                v-model:file-list="{[ name ]}ImageList"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                list-type="picture-card"
                :on-preview="handle{[ name | upper ]}PictureCardPreview"
                :on-remove="handle{[ name | upper ]}PictureRemove"
              >
                <el-icon><Plus /></el-icon>
              </el-upload>
            {% elif field.type == "foreign-key" %}
            <el-select
              {% if field.formStaticProps %}v-bind="{[ name ]}Props"{% endif %}
              v-model="formData.{[ name ]}">
            </el-select>
            {% elif field.type == "many-to-many" %}
            {% endif %}
            {% endif %}
          </el-form-item>
        {% endfor %}
        <el-form-item>
          <el-button type="primary">保 存</el-button>
          <el-button>取 消</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    {% for name, field in fields.items() %}
    {% if field.type == 'image' %}
    <el-dialog v-model="{[ name ]}PreviewDialogVisible">
      <img w-full :src="{[ name ]}PreviewUrl" alt="{[ field.label or name ]}" />
    </el-dialog>
    {% endif %}
    {% endfor %}
  </div>

</template>

<script lang="ts" setup>
    import { reactive, ref } from 'vue';
    import { Plus } from '@element-plus/icons-vue'
    {% if image_field_exists %}
    import type { UploadProps, UploadUserFile } from 'element-plus'
    {% endif %} 
    
    defineOptions({
        name: "{[ (app_name + '-' + model_name) | camel_case_filter ]}CreateForm"
    });
    
    {% for name, field in fields.items() %}
    {% if field.formStaticProps %}
    const {[ name ]}Props = reactive({[ field.formStaticProps ]})
    {% endif %}
    {% if field.type == 'image' %}
    const {[ name ]}ImageList = reactive([])
    const {[ name ]}PreviewUrl = ref('')
    const {[ name ]}PreviewDialogVisible = ref(false)
    const handle{[ name | upper ]}PictureCardPreview: UploadProps['onPreview'] = (uploadFile) => {
      {[ name ]}PreviewUrl.value = uploadFile.url!
      {[ name ]}PreviewDialogVisible.value = true
    }
    const handle{[ name | upper ]}PictureRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
      console.log(uploadFile, uploadFiles)
    }
    {% endif %}
    {% endfor %}
    
    const formData = reactive({
        {% for name, field in fields.items() %}
        {% if field.creatable == False %}
        {% continue %}
        {% endif %}
        {[ name ]}: {[ default_value[name] ]}{% if not loop.last %},{% endif %}
        {% endfor %}
    })

    const onSubmit = () => {
        console.log('submit!')
    }
</script>

<style scoped>
    .el-form-item__content {
        max-width: 420px;
    }

    .form-card {
        min-height: 720px;
    }

    .el-select, .el-input, .el-input-number {
      width: 320px!important;
    }
</style>

