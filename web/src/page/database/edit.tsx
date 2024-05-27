import { DialogTitle, Divider } from '@mui/material';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import TextField from '@mui/material/TextField';
import { useForm, SubmitHandler } from 'react-hook-form';
import { injector } from '../../service/provider';
import { DatabaseService } from '../../service/database.service';
interface Inputs {
  database_type: string;
  database_name: string;
  db_path?: string;
  username?: string;
  password?: string;
  address?: string;
  port?: string;
  remark?: string;
}

export function DatabaseEdit(inputs: { data: any; setDialogOpen: (value: boolean) => any }) {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>({ defaultValues: inputs.data });
  let service = injector.get(DatabaseService);
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    service.saveData({ ...data, database_type: inputs.data.database_type, id: inputs.data.id }).then(() => {
      inputs.setDialogOpen(false);
    });
  };
  // 既然演示就先不做验证,反正只有开发者操作,
  // false/true部分为本地数据库和远程数据库的参数,也是先放着,反正演示
  return (
    <div className="">
      <DialogTitle>
        {inputs.data.id ? '编辑' : '新增'}
        {'数据库连接'}
      </DialogTitle>
      <Divider></Divider>

      <form onSubmit={handleSubmit(onSubmit)} className=" mt-2">
        <DialogContent>
          <div className="flex flex-col gap-4 w-[500px]">
            <TextField
              {...register('database_type', { required: true, disabled: true })}
              label="数据库类型"
              value={inputs.data.database_type}
            />
            <TextField {...register('database_name', { required: true })} label="数据库名" />
            {false && <TextField {...register('db_path', { required: true })} label="数据库名" />}
            {true && (
              <>
                <TextField {...register('username', { required: true })} label="用户名" />
                <TextField {...register('password', { required: false })} label="密码" type="password" />
                <TextField {...register('address', { required: true })} label="地址" />
                <TextField {...register('port', { required: true })} label="端口" />
              </>
            )}
            <TextField {...register('remark', { required: true })} label="备注" multiline />
          </div>
        </DialogContent>
        <Divider></Divider>

        <DialogActions>
          <Button variant="contained" type="submit">
            提交
          </Button>
          <Button variant="contained" type="button" color="error" onClick={() => inputs.setDialogOpen(false)}>
            关闭
          </Button>
        </DialogActions>
      </form>
    </div>
  );
}
