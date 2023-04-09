import {Module} from '@nestjs/common';
import {AppController} from './app.controller';
import {AppService} from './app.service';
import {ServeStaticModule} from '@nestjs/serve-static';
import * as path from 'path';
import {TypeOrmModule} from "@nestjs/typeorm";
import {BusesModule} from "./buses/buses.module";

console.log(path.join(__dirname, '..', 'static'))
console.log(__dirname)

@Module({
    imports: [ TypeOrmModule.forRoot({
        type: 'postgres',
        host: 'db',
        port: 5432,
        username: 'postgres',
        password: 'ahan2004',
        database: 'qazvision',
        entities: ["dist/**/*.entity{.ts,.js}"],
        synchronize: true
    }),
        ServeStaticModule.forRoot({
            rootPath: path.join(__dirname, '..', 'static'),
            serveRoot: '/',
            exclude: ['/api*'],
        }), BusesModule],
    controllers: [AppController],
    providers: [AppService],
})
export class AppModule {
}
