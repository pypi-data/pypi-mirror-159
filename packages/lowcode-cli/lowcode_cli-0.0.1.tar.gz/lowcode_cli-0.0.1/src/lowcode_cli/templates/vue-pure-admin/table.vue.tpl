{% set fields = schema.properties.fields.properties %}
{% set field_names = get_field_names(schema) %}
{% set search_form_data = get_field_default_value(schema) %}
{% set app_name = schema.properties.app.app_name or '' %}
{% set model_name = schema.properties.model.name or '' %}
{% set searchable_fields = get_searchable_fields(schema) %}
{% set filterable_fields = get_filterable_fields(schema) %}

<template>
  <div>
    <el-card class="search-card">
      <el-form :inline="true" :model="searchFormData">
        {% if searchable_fields %}
        <el-form-item label="搜索">
          <el-input placeholder="请输入{[ searchable_fields | search_placeholder ]}"/>
        </el-form-item>
        {% endif %}
        <el-form-item label="Approved by">
          <el-input placeholder="Approved by"/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">重 置</el-button>
          <el-button type="primary">查 询</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <el-card class="table-card">
      <div class="opt-box">
        <div>
          <el-dropdown>
            <el-button>
              批量操作
              <el-icon class="el-icon--right">
                <arrow-down/>
              </el-icon>
            </el-button>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>批量删除</el-dropdown-item>
                <el-dropdown-item>批量导出</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
        <div>
          <el-button type="primary" @click="navigateToCreatePage">创 建</el-button>
          <el-button @click="handleExportTotal">导 出</el-button>
        </div>
      </div>
      <el-table :data="tableData" style="width: 100%">
        {% for name, field in fields.items() %}
          <el-table-column
              {% if field.tableStaticProps %}v-bind="{[ name ]}Props"{% endif %}
              prop="{[ name ]}"
              label="{[ field.label or name ]}"/>
        {% endfor %}
        <el-table-column
            fixed="right"
            label="操作"
            width="120">
          <template #default>
            <el-button type="primary" size="small" @click="navigateToProfilePage">
              详情
            </el-button>
            <el-button link type="primary" size="small" @click="navigateToEditPage">
              编辑
            </el-button>
            <el-popconfirm title="Are you sure to delete this?">
              <template #reference>
                <el-button link type="danger" size="small" @click="handleDelete">
                  删除
                </el-button>
              </template>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination-box">
        <el-pagination
            v-model:currentPage="pageConfig.pageNum"
            v-model:page-size="pageConfig.pageSize"
            :page-sizes="pageConfig.pageSizes"
            background
            layout="sizes, prev, pager, next, total"
            :total="pageConfig.total"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
    import {reactive, ref} from 'vue'
    import {ArrowDown} from '@element-plus/icons-vue'

    defineOptions({
        name: "{[ (app_name + '-' + model_name) | camel_case_filter ]}"
    });
    
    {% for name, field in fields.items() %}
    {% if field.tableStaticProps %}
    const {[ name ]}Props = reactive({[ field.tableStaticProps ]})
    {% endif %}
    {% endfor %}

    // 搜索栏
    const searchFormData = reactive({
    {% for name, field_default in search_form_data.items() %}
        {[ name ]}: {[ field_default ]}{% if not loop.last %},{% endif %}
    {% endfor %}
    })

    // 分页
    const pageConfig = reactive({
        pageNum: 1,
        pageSize: 20,
        pageSizes: [20, 50, 100, 200],
        total: 0
    })

    const handleSizeChange = (val: number) => {

    };
    const handleCurrentChange = (val: number) => {

    };

    // 跳转到表单页面
    const navigateToCreatePage = () => {

    };

    // 导出全量数据
    const handleExportTotal = () => {

    };

    // 跳转到详情页面
    const navigateToProfilePage = () => {

    };
    
    // 跳转到编辑页面
    const navigateToEditPage = () => {

    };

    // 删除记录
    const handleDelete = () => {

    }

    // 表格数据
    const tableData = reactive([])

</script>


<style lang="scss" scoped>
    .search-card {
        margin-bottom: 16px
    }

    .table-card {
        min-height: 520px;
        position: relative;
    }

    .pagination-box {
        float: right;
        padding: 16px 0;
        position: absolute;
        right: 0;
        bottom: 0;
    }

    .opt-box {
        display: flex;
        justify-content: space-between;
        padding: 0 12px;
        margin-bottom: 16px;
    }
</style>
