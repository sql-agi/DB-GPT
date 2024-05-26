import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Avatar from '@mui/material/Avatar';

import { DB_LIST } from '../const';
import Drawer from '@mui/material/Drawer';
import { useState } from 'react';
import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import Dialog from '@mui/material/Dialog';
import { DatabaseEdit } from './edit';
import { injector } from '../../service/provider';
import { DatabaseService } from '../../service/database.service';
import { useSignal } from '../../service/signal/use-signal';
import CardActions from '@mui/material/CardActions';
import Typography from '@mui/material/Typography';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import IconButton from '@mui/material/IconButton';
import Badge from '@mui/material/Badge';
import Divider from '@mui/material/Divider';

function DatabaseDetail(inputs: { dbType: string }) {
  const [dialogOpen, setDialogOpen] = useState(false);
  let databaseService = injector.get(DatabaseService);
  let list = useSignal(databaseService.databaseList).filter((item) => item.database_type === inputs.dbType);
  let [editData, setEditData] = useState({ database_type: inputs.dbType });
  return (
    <>
      <Dialog open={dialogOpen}>
        <DatabaseEdit data={editData} setDialogOpen={setDialogOpen}></DatabaseEdit>
      </Dialog>
      <h2 className="m-4 text-center text-lg">{inputs.dbType}</h2>
      <Divider></Divider>
      <div className="m-4 w-[400px]">
        {list.length ? (
          <div className="mb-4 flex flex-col gap-4">
            {list.map((item, index) => (
              <Card key={index}>
                <CardHeader title={item.database_name} />
                <CardContent>
                  {/* <Typography>用户名:{item.username}</Typography>
              <Typography>地址:{item.address}</Typography>
              <Typography>端口:{item.port}</Typography> */}
                  <Typography>备注:{item.remark}</Typography>
                </CardContent>
                <CardActions className="flex gap-4">
                  <div className="flex-1"></div>
                  <IconButton
                    size="small"
                    onClick={() => {
                      databaseService.getItem(item.id).then((item) => {
                        console.log(item);

                        setEditData({ ...item });
                        setDialogOpen(true);
                      });
                    }}
                  >
                    <EditIcon></EditIcon>
                  </IconButton>
                  <IconButton
                    size="small"
                    color="error"
                    onClick={() => {
                      databaseService.deleteItem(item.id);
                    }}
                  >
                    <DeleteIcon></DeleteIcon>
                  </IconButton>
                </CardActions>
              </Card>
            ))}
          </div>
        ) : null}

        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => {
            setEditData({ database_type: inputs.dbType });
            setDialogOpen(true);
          }}
          className="w-full"
        >
          创建连接
        </Button>
      </div>
    </>
  );
}

export function Database() {
  const [open, setOpen] = useState(false);
  let [dbType, setDbType] = useState('');
  const toggleDrawer = (newOpen: boolean, type?: string) => () => {
    if (type) {
      setDbType(type);
    }
    setOpen(newOpen);
  };
  let databaseService = injector.get(DatabaseService);
  /** 数据库列表，可以返回比较哪些支持，哪些不支持 */
  databaseService.requestList();
  let dataList = useSignal(databaseService.databaseList);
  return (
    <>
      <Drawer open={open} onClose={toggleDrawer(false)} anchor="right">
        {<DatabaseDetail dbType={dbType}></DatabaseDetail>}
      </Drawer>
      <div className="grid grid-cols-4 gap-4 w-[80%] mx-auto ">
        {DB_LIST.map((item, index) => {
          let connectedList = dataList.filter((dataItem) => {
            return dataItem.database_type === item[0];
          }).length;
          return (
            <div key={index} onClick={toggleDrawer(true, item[0])} className="hover:cursor-pointer">
              <Badge badgeContent={connectedList} invisible={!connectedList} color="success" className="block w-full">
                <Card sx={{ '&:hover': { boxShadow: 6 } }} className="w-full">
                  <CardHeader title={item[1].label} avatar={<Avatar src={item[1].icon}></Avatar>}></CardHeader>
                  <CardContent className="h-[100px]">{item[1].desc}</CardContent>
                </Card>
              </Badge>
            </div>
          );
        })}
      </div>
    </>
  );
}
