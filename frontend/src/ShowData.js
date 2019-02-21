import React from 'react'
import { Table, } from 'antd';

const columns = [{
  title: 'Campaign Name',
  dataIndex: 'campaignId.name',
  key: 'name',
  render: text => <a href="javascript:;">{text}</a>,
},{
  title: 'CL Name',
  dataIndex: 'clId.name',
  key: 'clname',
},{
  title: 'CL district',
  dataIndex: 'clId.district.name',
  key: 'cldistrict',
},{
  title: 'CL Phone Number',
  dataIndex: 'clId.phone',
  key: 'clphone',
},{
  title: 'CL Name',
  dataIndex: 'agentId.name',
  key: 'clname',
},{
  title: 'CL district',
  dataIndex: 'agentId.district.name',
  key: 'cldistrict',
},{
  title: 'CL Phone Number',
  dataIndex: 'agentId.phone',
  key: 'clphone',
}];



export default function (props) {
    return(<Table columns={columns} dataSource={props.data} />)
}