import { DialogTitle } from '@mui/material';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import TextField from '@mui/material/TextField';
import { useForm, SubmitHandler } from 'react-hook-form';
interface Inputs {
  db_type: string;
  db_name: string;
  db_path?: string;
  db_user?: string;
  db_pwd?: string;
  db_host?: string;
  db_port?: string;
  comment?: string;
}

export function DatabaseEdit(inputs: { dbType: string; setDialogOpen: (value: boolean) => any }) {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>();
  const onSubmit: SubmitHandler<Inputs> = (data) => console.log(data);
  // 既然演示就先不做验证,反正只有开发者操作,
  // false/true部分为本地数据库和远程数据库的参数,也是先放着,反正演示
  return (
    <div className="">
      <DialogTitle>{'新增数据库连接'}</DialogTitle>
      <form onSubmit={handleSubmit(onSubmit)} className=" mt-2">
        <DialogContent>
          <div className="flex flex-col gap-4 w-[500px]">
            <TextField {...register('db_type', { required: true, disabled: true })} label="数据库类型" value={inputs.dbType} />
            <TextField {...register('db_name', { required: true })} label="数据库名" />
            {false && <TextField {...register('db_path', { required: true })} label="数据库名" />}
            {true && (
              <>
                <TextField {...register('db_user', { required: true })} label="用户名" />
                <TextField {...register('db_pwd', { required: false })} label="密码" type="password" />
                <TextField {...register('db_host', { required: true })} label="地址" />
                <TextField {...register('db_port', { required: true })} label="端口" />
              </>
            )}
            <TextField {...register('comment', { required: true })} label="备注" multiline />
          </div>
        </DialogContent>
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
